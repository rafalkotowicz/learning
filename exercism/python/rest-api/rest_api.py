"""Exercism Rest API implementation."""

import json


class RestAPI:
    """Simple in-memory REST API for users and IOUs."""

    USERS_URL = "/users"
    ADD_URL = "/add"
    IOU_URL = "/iou"

    def __init__(self, database=None):
        self.database = database or {"users": []}

    def get(self, url, payload=None):
        """Handle GET requests."""
        if url != self.USERS_URL:
            raise ValueError(f"Unsupported endpoint: {url}")

        users = self._users_from_payload(payload)

        return json.dumps({"users": self._sorted_users(users)})

    def post(self, url, payload=None):
        """Handle POST requests."""
        data = self._parse_payload(payload)

        if url == self.ADD_URL:
            user = self._new_user(data["user"])
            self.database["users"].append(user)
            return json.dumps(user)

        if url == self.IOU_URL:
            lender = self._find_user(data["lender"])
            borrower = self._find_user(data["borrower"])
            amount = float(data["amount"])
            self._register_iou(lender, borrower, amount)
            self._recalculate_balance(lender)
            self._recalculate_balance(borrower)
            return json.dumps({"users": self._sorted_users([lender, borrower])})

        raise ValueError(f"Unsupported endpoint: {url}")

    @staticmethod
    def _parse_payload(payload):
        return json.loads(payload or "{}")

    def _find_user(self, name):
        user = next(
            (entry for entry in self.database["users"] if entry["name"] == name), None
        )
        if user is None:
            raise ValueError(f"User not found: {name}")
        return user

    def _users_from_payload(self, payload):
        if payload is None:
            return self.database["users"]
        requested_names = set(self._parse_payload(payload)["users"])
        return [
            user for user in self.database["users"] if user["name"] in requested_names
        ]

    @staticmethod
    def _new_user(name):
        return {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}

    @staticmethod
    def _sorted_users(users):
        return sorted(users, key=lambda user: user["name"])

    @staticmethod
    def _register_iou(lender, borrower, amount):
        reverse_debt = lender["owes"].get(borrower["name"], 0.0)

        if reverse_debt > 0:
            if reverse_debt > amount:
                remaining_reverse = reverse_debt - amount
                lender["owes"][borrower["name"]] = remaining_reverse
                borrower["owed_by"][lender["name"]] = remaining_reverse
                return

            del lender["owes"][borrower["name"]]
            del borrower["owed_by"][lender["name"]]
            amount -= reverse_debt

        if amount > 0:
            existing_debt = borrower["owes"].get(lender["name"], 0.0)
            new_debt = existing_debt + amount
            borrower["owes"][lender["name"]] = new_debt
            lender["owed_by"][borrower["name"]] = new_debt

    @staticmethod
    def _recalculate_balance(user):
        user["balance"] = sum(user["owed_by"].values()) - sum(user["owes"].values())

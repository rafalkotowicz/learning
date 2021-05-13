class User:
    n_active = 0
    users = []

    def __init__(self, active: bool, user_name: str):
        self.active = active
        self.user_name = user_name

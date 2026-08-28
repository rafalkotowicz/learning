"""Utilities for creating and formatting ledger entries."""

# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime


HEADERS = {
    "en_US": "Date       | Description               | Change       ",
    "nl_NL": "Datum      | Omschrijving              | Verandering  ",
}

DATE_FORMATS = {
    "en_US": "%m/%d/%Y",
    "nl_NL": "%d-%m-%Y",
}


@dataclass
class LedgerEntry:
    date: datetime
    description: str
    change: int


def create_entry(date, description, change):
    """Create a ledger entry from an ISO date, description, and cent value."""
    return LedgerEntry(
        date=datetime.strptime(date, "%Y-%m-%d"),
        description=description,
        change=change,
    )


def format_entries(currency, locale, entries):
    """Return ledger rows sorted and formatted for the requested locale and currency."""
    sorted_entries = sorted(entries, key=lambda entry: (entry.date, entry.description, entry.change))
    header = HEADERS[locale]
    formatted_rows = [header]

    for entry in sorted_entries:
        formatted_date = entry.date.strftime(DATE_FORMATS[locale])
        formatted_description = _format_description(entry.description)
        formatted_change = _format_change(entry.change, currency, locale)
        formatted_rows.append(f"{formatted_date} | {formatted_description} | {formatted_change}")

    return "\n".join(formatted_rows)


def _format_description(description):
    if len(description) > 25:
        return description[:22] + "..."
    return description.ljust(25)


def _format_change(change_in_cents, currency, locale):
    currency_symbol = "$" if currency == "USD" else "\u20ac"
    absolute_cents = abs(change_in_cents)
    major_units = absolute_cents // 100
    cents = absolute_cents % 100

    if locale == "en_US":
        formatted_number = f"{major_units:,}.{cents:02d}"
        if change_in_cents < 0:
            value = f"({currency_symbol}{formatted_number})"
        else:
            value = f"{currency_symbol}{formatted_number} "
    else:
        formatted_major_units = f"{major_units:,}".replace(",", ".")
        formatted_number = f"{formatted_major_units},{cents:02d}"
        sign = "-" if change_in_cents < 0 else ""
        value = f"{currency_symbol} {sign}{formatted_number} "

    return value.rjust(13)

"""Translate delivery date descriptions into concrete datetimes."""

import calendar
from datetime import date, datetime, time, timedelta

NOW_DESCRIPTION = "NOW"
ASAP_DESCRIPTION = "ASAP"
END_OF_WEEK_DESCRIPTION = "EOW"
MONTH_SUFFIX = "M"
QUARTER_PREFIX = "Q"

WORKDAY_END_HOUR = 17
MIDDAY_HOUR = 13
SUNDAY_EVENING_HOUR = 20
MORNING_HOUR = 8
TWO_HOUR_DELTA = 2

WEDNESDAY_INDEX = 2
FRIDAY_INDEX = 4
SATURDAY_INDEX = 5
SUNDAY_INDEX = 6


def delivery_date(start: str, description: str) -> str:
    """Return a delivery date in ISO format based on the meeting start and shorthand description."""
    meeting_start = datetime.fromisoformat(start)

    if description == NOW_DESCRIPTION:
        return _format_datetime(meeting_start + timedelta(hours=TWO_HOUR_DELTA))

    if description == ASAP_DESCRIPTION:
        return _handle_asap(meeting_start)

    if description == END_OF_WEEK_DESCRIPTION:
        return _handle_end_of_week(meeting_start)

    if description.endswith(MONTH_SUFFIX) and description[:-1].isdigit():
        target_month_number = int(description[:-1])
        return _handle_target_month(meeting_start, target_month_number)

    if description.startswith(QUARTER_PREFIX) and description[1:].isdigit():
        target_quarter_number = int(description[1:])
        return _handle_target_quarter(meeting_start, target_quarter_number)

    raise ValueError("Unsupported delivery description")


def _handle_asap(meeting_start: datetime) -> str:
    if meeting_start.time() < time(hour=MIDDAY_HOUR):
        delivery_datetime = datetime.combine(
            meeting_start.date(), time(hour=WORKDAY_END_HOUR)
        )
        return _format_datetime(delivery_datetime)

    next_day = meeting_start.date() + timedelta(days=1)
    delivery_datetime = datetime.combine(next_day, time(hour=MIDDAY_HOUR))
    return _format_datetime(delivery_datetime)


def _handle_end_of_week(meeting_start: datetime) -> str:
    if (weekday_number := meeting_start.weekday()) <= WEDNESDAY_INDEX:
        day_delta = FRIDAY_INDEX - weekday_number
        delivery_day = meeting_start.date() + timedelta(days=day_delta)
        delivery_datetime = datetime.combine(delivery_day, time(hour=WORKDAY_END_HOUR))
        return _format_datetime(delivery_datetime)

    day_delta = SUNDAY_INDEX - weekday_number
    delivery_day = meeting_start.date() + timedelta(days=day_delta)
    delivery_datetime = datetime.combine(delivery_day, time(hour=SUNDAY_EVENING_HOUR))
    return _format_datetime(delivery_datetime)


def _handle_target_month(meeting_start: datetime, target_month_number: int) -> str:
    if not 1 <= target_month_number <= 12:
        raise ValueError("Month description out of range")

    meeting_month_number = meeting_start.month
    target_year_number = meeting_start.year
    if meeting_month_number >= target_month_number:
        target_year_number += 1

    first_day = date(target_year_number, target_month_number, 1)
    first_workday = _next_workday(first_day)
    delivery_datetime = datetime.combine(first_workday, time(hour=MORNING_HOUR))
    return _format_datetime(delivery_datetime)


def _handle_target_quarter(meeting_start: datetime, target_quarter_number: int) -> str:
    if not 1 <= target_quarter_number <= 4:
        raise ValueError("Quarter description out of range")

    meeting_quarter_number = ((meeting_start.month - 1) // 3) + 1
    target_year_number = meeting_start.year
    if meeting_quarter_number > target_quarter_number:
        target_year_number += 1

    quarter_last_month_number = target_quarter_number * 3
    quarter_last_day_number = calendar.monthrange(
        target_year_number, quarter_last_month_number
    )[1]
    quarter_last_day = date(
        target_year_number, quarter_last_month_number, quarter_last_day_number
    )
    quarter_last_workday = _previous_workday(quarter_last_day)
    delivery_datetime = datetime.combine(quarter_last_workday, time(hour=MORNING_HOUR))
    return _format_datetime(delivery_datetime)


def _next_workday(candidate_day: date) -> date:
    while candidate_day.weekday() >= SATURDAY_INDEX:
        candidate_day += timedelta(days=1)
    return candidate_day


def _previous_workday(candidate_day: date) -> date:
    while candidate_day.weekday() >= SATURDAY_INDEX:
        candidate_day -= timedelta(days=1)
    return candidate_day


def _format_datetime(moment: datetime) -> str:
    return moment.isoformat(timespec="seconds")

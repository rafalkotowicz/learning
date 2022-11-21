from datetime import date


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    day_to_int: {str, int} = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    days_in_month = []
    for day in range(1, 32):
        _date = None
        try:
            _date = date(year, month, day)
        except:
            break
        if _date.weekday() == day_to_int[day_of_week]:
            days_in_month.append(day)

    if week == "first":
        wanted_day = days_in_month[0]
    elif week == "second":
        wanted_day = days_in_month[1]
    elif week == "third":
        wanted_day = days_in_month[2]
    elif week == "fourth":
        wanted_day = days_in_month[3]
    elif week == "fifth":
        try:
            if days_in_month[4]:
                wanted_day = days_in_month[4]
        except IndexError:
            raise MeetupDayException("That day does not exist.")
    elif week == "last":
        wanted_day = days_in_month[-1]
    elif week == "teenth":
        wanted_day = [day for day in days_in_month if 13 <= day <= 19].pop()

    return date(year, month, wanted_day)

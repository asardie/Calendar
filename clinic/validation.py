import datetime
import re


def is_time_valid(time):
    """
    checks to see if a time is within a givent the range 7am to 6pm
    """
    start = datetime.time(7, 0, 0)
    end = datetime.time(18, 0, 0)
    if time >= start and time < end:
        return True
    else:
        return False


def day_of(time):
    """
    checks what day of the week it is or will be on a specific date
    """
    return time.weekday()


def print_day(day):
    """
    return the day as text
    0 is monday and 6 is sunday
    """
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[day].lower()


def is_email_wethinkcode(email):
    """
    checks if email is a WETHINKCODE email
    """
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]?[student.]*wethinkcode.co.za$'
    return True if re.search(regex,email) else False


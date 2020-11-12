import datetime

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
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[day]

# print(day_of(datetime.datetime(2020, 11, 9, 7, 0, 0)))
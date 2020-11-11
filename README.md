# Calendar

tasks: #if you complete a task. It will be removed it once code has been merged

-> please, edit this file and make a pull request.("you can just add your name")
        
        sinazo :)

-> Read up on argparse {python3 module}. WILL BE IMPORTANT.

-> We need a function that checks to see if a time is within a givent range, eg: between 7am and 6pm.
    this function should take in a time {datetime.datetime} as an argument.(see python3 datetime module)
    and return True if it is within the range and false if it is not.
    
    prototype: def is_time_valid(time) -> bool:
    arg: time {datetime.datetime}
    return:  valid_time {bool}
    
-> We need a function that checks what day of the week it is or will be on a specific date.
    
    prototype: def day_of(time: datetime.datetime) -> string/int:
    arg: time {datetime.datetime}
    return: int 1-7 numbering the days from monday(1) to sunday(7)
    
-> We need a function that return the day as text:
    
    prototype: def print_day(day: int) -> text:
    arg: day {int}
    return: return day. {string} returns the day of the week as 'monday', 'tuesday', 'wednesday', etc
    
-> We need a function to check the users 'primary' calendar to see if they are free or busy:

    prototype: def is_free(time: datetime.datetime) -> bool:
    args: time {datetime.datetime}
    return (True if free and False if not)
    references: https://developers.google.com/calendar/v3/reference/freebusy
                https://developers.google.com/calendar/v3/reference/freebusy/query
                
    
------------------------------------------------------------------------------

What we need:
-------------
We Still need a main...

Some Way of getting user input

Some way of validating input from the user.

And any sense of structure


DESIGN NOTES:
-------------

CALENDAR: {package}

    -> read_events.py   {module}
    -> create_events.py {module}
    -> set_up.py        {module}
    
    AUTHENTICATION: {sub-package}
    
        -> auth.py      {module}
    
main.py {module}

# Calendar

tasks: #if you complete a task. It will be removed it once code has been merged

-> please, edit this file and make a pull request.("you can just add your name")

-> We need a function that checks to see if a time is within a givent range, eg: between 7am and 6pm.
    this function should take in a time {datetime.datetime} as an argument.(see python3 datetime module)
    and return True if it is within the range and false if it is not.
    
    prototype: def is_time_valid(time) -> bool:
    arg: time {datetime.datetime}
    return:  valid_time {bool}
    
-> We need a function that checks what day of the week it is or will be on a specific date.
    
    prototype: def day_of(time: datetime.datetime) -> string/int:
    arg: time {datetime.datetime}
    return: string('monday', 'tuesday', etc) or int 1-7 numbering the days from monday(1) to sunday(7)
------------------------------------------------------------------------------

What we need:
-------------
We Still need a main...

Some Way of getting user input

Some way of validating input from the user.

And any sense of structure


DESIGN NOTES:
-------------

CALENDAR:

    -> read_events.py
    -> create_events.py
    -> set_up.py
    
    AUTHENTICATION:
    
        -> auth.py -> file with create_service():
    ---------------
    
main.py

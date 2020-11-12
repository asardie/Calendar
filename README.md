# Calendar

tasks: #if you complete a task. It will be removed it once code has been merged

-> please, edit this file and make a pull request.("you can just add your name")
        
        sinazo :)

-> Read up on argparse {python3 module}. WILL BE IMPORTANT.
    
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

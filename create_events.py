import datetime
import users
import view_events
import auth

def get_time():
    time = input('would you like to volunteer in the morning or afternoon (AM/pm)?: ')
    while 1:
        if time.lower() == 'am':
            posible_times = [(datetime.time(hour=i//60, minute=(i%60))) for i in range(7*60, 12*60, 15)]
            break
        elif time.lower() == 'pm':
            posible_times = [(datetime.time(hour=i//60, minute=(i%60))) for i in range(12*60, 17*60, 15)]
            break
        else:
            time = input("please enter am or pm: ")

    for i, time in enumerate(posible_times):
        print(i, time, sep=' : ')

    while 1:
        t = input("enter a time id: (0,1,2,3,etc): ")
        if t.isdigit():
            return posible_times[int(t)]

    

    

def add_to_clinic_calander():
    shared_service = auth.create_shared_service()

    time = get_time()

    event = {
    'summary': f"{' - '.join(['code_clinic', users.get_username()])}",
    'location': f"{input('jhb or cpt: ')}",
    'description': f"{input('What topics are you willing to cover: ')}",
    'start': {
        'dateTime': '2015-05-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2015-05-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles'
    }}

    event = shared_service.events().insert(calendarId='primary', body=event).execute()


print(get_time())
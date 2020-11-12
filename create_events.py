import datetime
import users
import view_events
import auth

def add_to_clinic_calander():
    shared_service = auth.create_shared_service()

    posible_times = [f"{i}:00" for i in range(7,16)]


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

posible_times = [(datetime.timedelta(hours=i)) for i in range(7, 16)]

for p in posible_times:
    print(p)
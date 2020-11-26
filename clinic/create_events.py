import datetime
import clinic
import clinic.validation as validation


def get_time():
    """
    converts user input from string to datetime object.
    """
    year = datetime.datetime.now().year

    while 1:
        date = input("What date would you like to volunteer? (mm/dd) ")
        time = input("What time would you like to volunteer? (hh:mm) ")

        time = '/'.join([str(year), date, time])
        time = datetime.datetime.strptime(time, '%Y/%m/%d/%H:%M')
        while not validation.is_time_valid(time.time()):
            time = input("Please enter time between 7:00 and 18:00 in the following format(hh:mm) ")
            time = '/'.join([str(year), date, time])
            time = datetime.datetime.strptime(time, '%Y/%m/%d/%H:%M')
        return time


def add_to_clinic_calander(time: datetime.datetime):
    shared_service = clinic.create_shared_service()

    desc = input('What topics are you willing to cover: ')
    for i in range(1):
        start = (time + datetime.timedelta(minutes=30*i))
        end = (time + datetime.timedelta(minutes=30))

        event = {
            'summary': f"{' - '.join(['code_clinic', clinic.get_username()])}",
            'location': "WeThinkCode_HQ",
            'description': f"{desc}",
            'start': {
                'dateTime': start.isoformat() + "+02:00",
            },
            'end': {
                'dateTime': end.isoformat()+"+02:00",
            },
            'maxAttendees': 2,
            'attendees': [
                {'email': f"{clinic.get_email()}",
                 'organiser': True}
            ],
            'anyoneCanAddSelf': True,
        }

        event = shared_service.events().insert(calendarId='primary',
                                               body=event).execute()


def add_as_attendee(service, id):
    event = service.events().get(calendarId='primary',
                                        eventId=id).execute()
    event['attendees'] += ([{'email': f"test.{clinic.get_email()}"}])

    service.events().update(calendarId='primary',
                            eventId=event['id'], body=event).execute()

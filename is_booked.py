import auth

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def is_booked(date_time):
    """
    Retuns true if the slot is booked.
    """
    bookings = {}
    auth.create_service()

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date')) 
        bookings[start[:10]] = start[11:16]

    for date_booked in bookings:
        if date_booked == date_time[11:16]:
            if date_time[:10] == bookings[date_booked]:
                return True
        return False

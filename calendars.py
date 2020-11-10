import auth
import datetime


def list_all_calendars():
    """
    lists all the calendars that belong to the logged in user.
    """
    service = auth.create_service()
    pt = None
    while 1:
        cal = service.calendarList().list(pageToken=pt).execute()
        for c in cal['items']:
            print(c['summary'], c['id'], sep=' : ')
        pt = cal.get('nexPageToken')
        if not pt:
            break


def list_events():
    """Lists all events for the next seven days
    """

    s = datetime.datetime.now().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    e = (datetime.datetime.now() + elapsed).isoformat() + 'Z'

    service = auth.create_service()

    pt = None
    while 1:
        events = service.events().list(calendarId='primary',
                                       timeMin=s,
                                       timeMax=e, pageToken=pt).execute()
        for ev in events['items']:
            print(ev['summary'], ev['id'])
        pt = events.get('nextPageToken')
        if not pt:
            break


def get_event(id=None):
    service = auth.create_service()
    id = '4btsiajm17usupgkou04vdni3i'
    ev = service.events().get(calendarId='primary',
                              eventId=id).execute()
    # print(ev['attendees'])
    for i, a in enumerate(ev['attendees']):
        if 'self' in a:
            ev['attendees'][i]['responseStatus'] = 'accepted'

    nev = service.events().update(calendarId='primary',
                                  eventId=id, body=ev).execute()

    for i, a in enumerate(nev['attendees']):
        print(a)



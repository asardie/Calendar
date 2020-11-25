import datetime
import clinic.view_events as events


def print_events(available, service):

    a = 'id', ' summary'+' '*13, ' topics'+' '*23, ' date'+' '*5, ' time'+' '*3, ' status' + ' '*5

    print(f" |{'-'*100}|")
    print('', *a, '', sep=' | ')
    print(f" |{'-'*100}|")
    for i, av in enumerate(available):
        date, time = av['start']['dateTime'].split('T')
        time = time.split('+')[0]
        length = len(av['description'])
        id_n = str(i)+' '*(2-len(str(i)))
        if not events.is_booked(av['id'], service):
            available = "Available   "
        else:
            available = "Booked      "
        a = id_n, av['summary'], av['description']+' '*(30-length), date, time, available
        print('', *a, '', sep=' | ')
        print(f" |{'-'*100}|")


def print_days():
    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']

    time = datetime.datetime.now()

    print('-'*25)
    for i in range(7):
        date = time + datetime.timedelta(days=i)
        day = date.weekday()

        print(days[day] + ' '*(9-len(days[day])),
              date.isoformat().split('T')[0], sep=':     ')
        print('-'*25)

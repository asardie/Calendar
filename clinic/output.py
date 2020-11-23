import datetime


def print_events(available):

    a = 'id', ' summary'+' '*13, ' topics'+' '*23, ' date'+' '*5, ' time'+' '*3

    print(f" |{'-'*85}|")
    print('', *a, '', sep=' | ')
    print(f" |{'-'*85}|")
    for i, av in enumerate(available):
        date, time = av['start']['dateTime'].split('T')
        time = time.split('+')[0]
        length = len(av['description'])
        id_n = str(i)+' '*(2-len(str(i)))
        a = id_n, av['summary'], av['description']+' '*(30-length), date, time
        print('', *a, '', sep=' | ')
        print(f" |{'-'*85}|")


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

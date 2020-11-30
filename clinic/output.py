import datetime
import clinic.view_events as events

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_events(available, service):

    a = 'id', ' summary'+' '*13, ' topics'+' '*23
    a += ' date'+' '*5, ' time'+' '*3, ' status' + ' '*5

    print(f" |{'-'*100}|")
    print('', *a, '', sep=' | ')
    print(f" |{'-'*100}|")
    for i, av in enumerate(available):
        date, time = av['start']['dateTime'].split('T')
        time = time.split('+')[0]
        length = len(av['description'])
        id_n = str(i)+' '*(2-len(str(i)))
        if not events.is_booked(av):
            # available = f"{bcolors.OKCYAN}Available   "{bcolors.ENDC}"
            available = f"{bcolors.OKGREEN}Available   {bcolors.ENDC}"
        else:
            available = f"{bcolors.FAIL}Booked      {bcolors.ENDC}"
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

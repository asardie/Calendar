import clinic
import datetime
import sys


def volunteer():
    time = clinic.get_time()
    clinic.add_to_clinic_calander(time)


def create_booking():
    """
    Allows a user to list the currently running clinics for the next
    7 days and choose a clinic to be a part of.

    """
    shared_service = clinic.create_shared_service()
    available = clinic.list_events(shared_service)

    a = 'summary'+' '*14, 'topics'+ ' '*24, 'date'+' '*6, 'time'

    print(f" |{'-'*80}|")
    print('',*a,'', sep=' | ')
    print(f" |{'-'*80}|")
    for i, av in enumerate(available):
        date, time = av['start']['dateTime'].split('T')
        a = av['summary'], av['description']+' '*(30-len(av['description'])), date, time.split('+')[0]
        print('', *a, '', sep=' | ')
        print(f" |{'-'*80}|")

    return
    booking_id = input('Which code clinic would you like attend?: ')
    booking = available[int(booking_id)]
    clinic.update_event(booking[-1])

    print("booking has been created... <3")
create_booking()

def run_clinic():
    args = [s.lower() for s in sys.argv]

    if 'volunteer' in args:
        volunteer()
    elif 'make_booking' in args:
        create_booking()
    elif 'init' in args:
        clinic.user_init()


if __name__ == "__main__":
    run_clinic()

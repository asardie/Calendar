import clinic
import datetime
import sys


def volunteer():
    time = clinic.get_time()
    day = clinic.get_date()
    volunteer_time = datetime.datetime.combine(day, time)
    clinic.add_to_clinic_calander(volunteer_time)


def create_booking():
    shared_service = clinic.create_shared_service()
    available = clinic.list_events(shared_service)
    for i, av in enumerate(available):
        date, time = av[2]['dateTime'].split('T')
        day = clinic.day_of(datetime.datetime.strptime(date, '%Y-%m-%d'))
        day = clinic.print_day(day)
        a = f"{i}-{av[0]},     date: {day}{' '*(9-len(day))}-{date}     "
        b = f"time: {time.split('+')[0]}     coverd topics: {av[1]},"
        print(a+b)

    booking_id = input('Which code clinic would you like attend?: ')
    booking = available[int(booking_id)]
    clinic.update_event(booking[-1])

    print("booking has been created... <3")


def run_clinic():
    args = [s.lower() for s in sys.argv]

    if 'volunteer' in args:
        volunteer()
    elif 'make_booking' in args:
        create_booking()
    elif 'init' in args:
        clinic.user_init()


if __name__ == "__main__":
    # run_clinic()
    clinic.get_time()

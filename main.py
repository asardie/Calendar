import clinic
import sys


def volunteer():
    """
    allows a user to specify a time and date to volunteer as a code clinicion
    """
    print("Here are the next 7 days for reference: ")
    clinic.print_days()

    time = clinic.get_time()
    clinic.add_to_clinic_calander(time)


def create_booking():

    """
    Allows a user to list the currently running clinics for the next
    7 days and choose a clinic to be a part of.
    """

    shared_service = clinic.create_shared_service()
    available = clinic.list_events(shared_service)

    clinic.print_events(available, shared_service)

    booking_id = input('Please enter a booking ID: ')
    booking = available[int(booking_id)]
    while 
    clinic.add_as_attendee(shared_service, booking['id'])

    print("booking has been created... <3")


def view_bookings():
    """
    allows the user to view the next seven days on their personal calendar.
    """
    service = clinic.create_service()
    f = clinic.list_events(service)
    clinic.print_events(f, service)


def run_clinic():
    args = [s.lower() for s in sys.argv]

    if 'volunteer' in args:
        volunteer()
    elif 'make_booking' in args:
        create_booking()
    elif 'view_bookings' in args:
        view_bookings()
    elif 'init' in args:
        clinic.user_init()


if __name__ == "__main__":
    run_clinic()

import clinic
import sys


def volunteer():
    """
    allows a user to specify a time and date to volunteer as a code clinicion
    """
    time = clinic.get_time()
    clinic.add_to_clinic_calander(time)


def create_booking():
    """
    Allows a user to list the currently running clinics for the next
    7 days and choose a clinic to be a part of.

    """
    shared_service = clinic.create_shared_service()
    available = clinic.list_events(shared_service)

    clinic.print_events(available)

    booking_id = input('Please enter a booking ID: ')
    booking = available[int(booking_id)]
    clinic.add_as_attendee(shared_service, booking['id'])

    print("booking has been created... <3")


def view_bookings():

    service = clinic.create_service()
    f = clinic.list_events(service)
    clinic.print_events(f)


def run_clinic():
    args = [s.lower() for s in sys.argv]

    if 'volunteer' in args:
        volunteer()
    elif 'make_booking' in args:
        create_booking()
    elif 'view' in args:
        view_bookings()
    elif 'init' in args:
        clinic.user_init()


if __name__ == "__main__":
    run_clinic()

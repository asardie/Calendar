import clinic
import sys
import clinic.view_events as events


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
    if len(booking['attendees']) < 2:
        clinic.add_as_attendee(shared_service, booking['id'])
        print("booking has been created... <3")
    else:
        print("slot already booked...")


def view_bookings():
    """
    allows the user to view the next seven days on their personal calendar.
    """
    service = clinic.create_service()
    f = clinic.list_events(service)
    clinic.print_events(f, service)


def cancel_patient():
    '''
    removes the patient (the last appended attendee)
    from the attendee list to an event
    '''

    service = clinic.create_service()
    shared_service = clinic.create_shared_service()
    ev = clinic.list_events(service)
    clinic.print_events(ev, service)
    ev_id = input("please enter an event Id to cancel: ")
    ev_id = int(ev_id)

    event = shared_service.events().get(calendarId='primary',
                                        eventId=ev[ev_id]['id']).execute()

    event['attendees'].pop()

    shared_service.events().update(calendarId='primary',
                                   eventId=ev[ev_id]['id'],
                                   body=event).execute()
    print("Successfully cancelled the booking")


def cancel_doctor():
    """
    Checks if the event the doctor wants to delete is not yet booked by a 
    patient and if not; deletes it.
    """
    
    service = clinic.create_service()
    shared_service = clinic.create_shared_service()
    ev = clinic.list_events(service)
    clinic.print_events(ev, service)
    ev_id = input("please enter a appointment Number to cancel: ")
    event = shared_service.events().get(calendarId='primary',
                                        eventId=ev[int(ev_id)]['id']).execute()
    if events.is_booked(event):
        print("You may not cancel an appointment that is already booked by a patient")
    else:
        shared_service.events().delete(calendarId='primary', eventId=ev[int(ev_id)]['id']).execute()
        print("Successfully cancelled the appointment")



def do_help():
    # TODO
    pass


def run_clinic():
    args = [s.lower() for s in sys.argv]

    if 'volunteer' in args:
        volunteer()
    elif 'make_booking' in args:
        create_booking()
    elif 'view_bookings' in args:
        view_bookings()
    elif 'cancel' in args:
        cancel_patient()
    elif 'delete' in args:
        cancel_doctor()
    elif 'help' in args or '-h' in args:
        do_help()
    elif 'init' in args:
        clinic.user_init()


if __name__ == "__main__":
    run_clinic()

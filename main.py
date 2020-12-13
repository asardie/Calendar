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
    print('your booking has been added, Thank You!')


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
    shared_service = clinic.create_shared_service()
    available = clinic.list_events(shared_service)
    clinic.print_events(available, shared_service)


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
    """
    Prints a detailed list of available commands and what they do
    """
    print(
    """
    Please provide some options
    usage: wtc-cal  [-h | --help]
                    <command>   [<args>]
    These are the wtc-cal commands that can be used in various situations:

    setup and login
                init    Registers the user, accesses their calender and keep them signed in

    Working with Code-Clinic
                volunteer       (for clinicians) voluteer 30 minutes to assist in someone's code
                make_booking    (for patients) book a timeslot wherein you will be helped with your code
                view_bookings   Show all bookings that have been made and in still available

    

    """)


def run_clinic():
    """
    This is the main function to run the clinic. 
    It dictates which functions to call based on user's command line input.
    """

    if len(sys.argv) == 1:
        do_help()
    elif sys.argv[1].lower() == 'volunteer':
        volunteer()
    elif sys.argv[1].lower() == 'make_booking':
        create_booking()
    elif sys.argv[1].lower() == 'view_bookings':
        view_bookings()
    elif sys.argv[1].lower() == 'cancel':
        cancel_patient()
    elif sys.argv[1].lower() == 'delete':
        cancel_doctor()
    elif sys.argv[1].lower() == 'help' or sys.argv[1].lower() == '-h' :
        do_help()
    elif sys.argv[1].lower() == 'init':
        clinic.user_init()
    else:
        do_help()


if __name__ == "__main__":
    run_clinic()

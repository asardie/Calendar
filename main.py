import argparse
import sys
import auth
import view_events
import create_events
import datetime

lst_flags = ["book_session", "volunteer", "available_slots", "start"]


def volunteer():
    time = create_events.get_time()
    day = create_events.get_date()
    volunteer_time = datetime.datetime.combine(day, time)
    create_events.add_to_clinic_calander(volunteer_time)

def create_booking():
    shared_service = auth.create_shared_service()
    available = view_events.list_events(shared_service)
    for av in available:
        print(f"{av[0]}, coverd topics: {av[1]}, time: {av[2]['dateTime']}")

create_booking()

def get_flag():

    flag = argparse.ArgumentParser(description='Run Code Clinic. Here is a list of valid commands:')
    flag.add_argument('init',help='Authenticates user')
    flag.add_argument('volunteer',help='Volunteer as a clinician')
    flag.add_argument('book_session',help='Book a session with an available clinician.')
    flag.add_argument('start', help='Runs the clinic application as a shell')

    # if flag not in lst_flags:
    #     return get_flag()
    
    return flag

def run_clinic():
    flag = get_flag()



if __name__ == "__main__":
    run_clinic()
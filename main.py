import argparse
import sys
import auth
import view_events
import create_events

lst_flags = ["book_session", "volunteer", "available_slots"]


def volunteer():
    time = create_events.get_time()
    day = create_events.get_date()
    
def get_flag():

    flag = argparse.ArgumentParser(description='Run Code Clinic. Here is a list of valid commands:')
    flag.add_argument('init',help='Authenticates user')
    flag.add_argument('volunteer',help='Volunteer as a clinician')
    flag.add_argument('book_session',help='Book a session with an available clinician.')

    if flag not in lst_flags:
        return get_flag()
    
    return flag

def run_clinic():
    flag = get_flag()

if __name__ == "__main__":
    run_clinic()
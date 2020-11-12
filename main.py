import argparse
import sys
import auth
import view_events
import create_events

lst_flags = ["book_session", "volunteer", "available_slots", "help"]


def volunteer():
    time = create_events.get_time()
    day = create_events.get_date()
    
def get_flag():
    flag = input("Are you booking a session or volunteering? (Type \'help\' for a list of available commands.) ").lower()
    if flag not in lst_flags:
        return get_flag()
    
    return flag

def get_help():
    
    print("Here is a list of valid commands:\n")
    print("\'help\' - Shows you this list.")
    print("\'book_session\' - Book a session with an available clinician.")
    print("\'volunteer\' - Volunteer as a clinician")

def run_clinic():
    flag = get_flag()

if __name__ == "__main__":
    run_clinic()

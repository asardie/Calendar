import json
import os

user_file = os.path.expanduser("~") + '/' + '.config/codeClinic/user.json'

def get_username():
    with open(user_file, "r") as f:
        user_info = json.load(f)

    return user_info['user_name']

def get_email():
    with open(user_file, "r") as f:
        user_info = json.load(f)

    return user_info['email']
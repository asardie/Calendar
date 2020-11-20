import os
import json


def make_path(path):
    """makes a path in the users home directory:

    args: path {string} -> required to create the path... ie: 'folder',
        will create path '~/folder'.
        'folder/subfolder' will create '~/folder/subfolder'

    no return
    """
    if not os.path.exists(path):
        os.makedirs(path)


def user_init():
    """Initial set up for user
    """

    user = os.path.expanduser('~')
    path = '.config/codeClinic'
    total_path = "/".join([user, path])

    make_path(total_path)

    # ----------------------GET USER INFO----------------------------
    user_info = {'email': f"{input('enter student email: ')}",
                 'user_name': f"{input('enter user_name: ')}",
                 }

    # ---------------------GET SHARED ACCESS TOKEN--------------------
    if not os.path.exists('shared_token.pickle'):
        print("downloading access token.")
        git_file = 'https://github.com/asardie/Calendar/raw/main/shared_token.pickle'
        os.system(f"wget {git_file} > ~/.config/codeClinic/shared_token.pickle")

    # ----------------------Write to file-----------------------------
    f = open(total_path+'/user.json', 'w')
    json.dump(user_info, f)
    f.close()

import os
import json
import auth
import requests
import pickle
import sys



def make_path(path):
    """makes a path in the users home directory:
    
    args: path {string} -> required to create the path... ie: 'folder',
        will create path '~/folder'.
        'folder/subfolder' will create '~/folder/subfolder'

    no return
    """
    user = os.path.expanduser('~')
    total_path = "/".join([user,path])
    if not os.path.exists(total_path):
        os.makedirs(total_path)


def user_init():
    """Initial set up for user
    """
    
    user = os.path.expanduser('~')
    path = '.config/codeClinic'
    total_path = "/".join([user,path])

    make_path(path)
    
    #----------------------GET USER INFO----------------------------
    user_info = {
        'user_name': input("enter student email: "),
    }

    #---------------------GET SHARED ACCESS TOKEN--------------------
    if not os.path.exists('shared_token.pickle'):
        print("downloading access token.")
        os.system("wget https://github.com/asardie/Calendar/raw/main/shared_token.pickle > ~/.config/codeClinic/shared_token.pickle")

    # ----------------------Write to file-----------------------------
    f = open(total_path+'/user.json', 'w')
    f.write(str(user_info))
    f.close()

user_init()
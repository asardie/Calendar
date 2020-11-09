import os
import json
import auth


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
    user_info = {
        'user_name': input("enter student email"),
    }
    f = open(total_path+'/user.json', 'w')
    f.write(str(user_info))
    f.close()

# if __name__ == "__main__":
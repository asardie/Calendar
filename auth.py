from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

client_secret = os.path.expanduser("~") + '/' + '.config/codeClinic/client_secret.json'
shared_token = os.path.expanduser("~") + '/' + '.config/codeClinic/shared_token.pickle'
client_token = os.path.expanduser("~") + '/' + '.config/codeClinic/token.pickle'
S = ['https://www.googleapis.com/auth/calendar']


def create_service():
    print(client_secret, client_token, shared_token, sep='\n')
    creds = None
    if os.path.exists(client_token):
        with open(client_token, 'rb') as token:
            creds = pickle.load(token)
            pass
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', S)
            creds = flow.run_local_server(port=0)

        with open(client_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

def create_shared_service():
    """
    creates a service token for the shared calendar.
    """
    shared_creds = None
    if not os.path.exists(shared_token):
        with open(shared_token, 'rb') as token:
            f = open(shared_token, 'wb')
            shared_creds = pickle.load(token)
            pickle.dump(shared_creds, f)
            f.close()
    else:
        print('need token.')

    if os.path.exists(shared_token):
        with open(shared_token, 'rb') as token:
            shared_creds = pickle.load(token)

    if not shared_creds or not shared_creds.valid:
        if shared_creds and shared_creds.expired and shared_creds.refresh_token:
            shared_creds.refresh(Request())

        with open(shared_token, 'wb') as token:
            pickle.dump(shared_creds, token)

    shared_service = build('calendar', 'v3', credentials=shared_creds)

    return shared_service        


create_service()
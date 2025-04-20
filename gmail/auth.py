import os
import pickle
import tempfile
import json
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# https://www.googleapis.com/auth/gmail.readonly - Solo lectura
# https://www.googleapis.com/auth/gmail.modify - Modificar pero no borrar
SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.readonly']


def create_credentials_file():
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')

    if not client_id or not client_secret:
        raise ValueError(
            "Environment variables GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET are required. "
            "Please, write them in your MCP config file."
        )

    credentials = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
            "project_id": ""
        }
    }

    fd, path = tempfile.mkstemp(suffix='.json')
    with os.fdopen(fd, 'w') as f:
        json.dump(credentials, f)

    return path

def authenticate_gmail():
    creds = None

    token_dir = os.path.join(Path.home(), '.gmail-mcp')
    os.makedirs(token_dir, exist_ok=True)
    token_path = os.path.join(token_dir, 'token.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            credentials_path = create_credentials_file()
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            os.unlink(credentials_path) #Esto es nuevo
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service
"""
Service that:
- List messages by criteria
- Get messages details
- Decode messages content
"""
import base64
from typing import List, Dict, Any
from googleapiclient.discovery import Resource

class GmailService:
    def __init__(self, service: Resource):
        self.service = service

    def list_messages(self, query='', max_results=10)-> List[Dict[str, Any]]:
        response = self.service.users().messages().list(userId='me', q=query, maxResults=max_results).execute()
        return response['messages']

    def get_message_details(self, message_id):
        response = self.service.users().messages().get(userId='me', id=message_id).execute()
        return {'headers': self._get_headers(response), 'body': self._get_body(response)}

    def get_labels(self):
        response = self.service.users().labels().list(userId='me').execute()
        return response['labels']

    @staticmethod
    def _get_headers(message):
        headers = message['payload']['headers']
        header_names = ['subject', 'from', 'to', 'cc', 'date']
        return_headers = {}
        for header in headers:
            if header['name'].lower() in header_names :
                return_headers[header['name'].lower()] = header['value']
        return return_headers

    @staticmethod
    def _get_body(message):
        if 'parts' in message['payload']:
            plain_text = None
            html = None

            for part in message['payload']['parts']:
                if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                    plain_text = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')

                elif part['mimeType'] == 'text/html' and 'data' in part['body']:
                    html = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')

            if plain_text:
                return plain_text
            elif html:
                return html
        elif 'body' in message['payload'] and 'data' in message['payload']['body']:
            data = base64.urlsafe_b64decode(message['payload']['body']['data']).decode('utf-8')
            return data

        return None
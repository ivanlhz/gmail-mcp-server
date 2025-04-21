"""
Service that:
- List messages by criteria
- Get messages details
- Decode messages content
"""
import base64
from typing import List, Dict, Any
from googleapiclient.discovery import Resource

from gmail.models.label_model import GmailLabel


class GmailService:
    def __init__(self, service: Resource):
        self.service = service

    def list_messages(self, query='', max_results=10, page_token=None):
        response = self.service.users().messages().list(userId='me', q=query, maxResults=max_results, pageToken=page_token).execute()
        return response

    def get_message_details(self, message_id):
        response = self.service.users().messages().get(userId='me', id=message_id).execute()
        return {'headers': self._get_headers(response), 'body': self._get_body(response)}

    def trash_message(self, message_id: str):
        response = self.service.users().messages().trash(userId='me', id=message_id).execute()
        return response

    def modify_message(self, msg_id:str, labels_to_remove: List[str], labels_to_add: List[str]):
        response = self.service.users().messages().modify(
            userId='me',
            id=msg_id,
            body={
                'removeLabelIds': labels_to_remove,
                'addLabelIds': labels_to_add,
            }
        ).execute()
        return response

    def batch_modify_message(self, msg_ids:List[str], labels_to_remove: List[str] = None, labels_to_add: List[str] = None):
        response = self.service.users().messages().batchModify(
            userId='me',
            body={
                'ids': msg_ids,
                'removeLabelIds': labels_to_remove,
                'addLabelIds': labels_to_add,
            }
        ).execute()
        return response

    def get_labels(self):
        response = self.service.users().labels().list(userId='me').execute()
        return response['labels']

    def get_label(self, label_id: str):
        response = self.service.users().labels().get(userId='me', id=label_id).execute()
        return response

    def create_label(self, label: GmailLabel):
        response = self.service.users().labels().create(userId='me',body=label.model_dump(exclude_none=True)).execute()
        return response

    def update_label(self, label_id: str, label: GmailLabel):
        response = self.service.users().labels().update(userId='me', id=label_id, body=label.model_dump(exclude_none=True)).execute()

        return response['label']
    def delete_label(self, label_id: str):
        response = self.service.users().labels().delete(userId='me',id=label_id).execute()
        return response

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
from mcp.server.fastmcp import FastMCP

from gmail.auth import authenticate_gmail
from gmail.service import GmailService

# Initialize FastMCP server
mcp = FastMCP("gmail-mcp-server")

@mcp.tool()
def get_emails_details(query: str):
    """Get emails details from gmail
    Args:
        query: gmail query string
    """
    try:
        api = authenticate_gmail()
        service = GmailService(api)
        results = service.list_messages(query)

        if not results:
            return []
        else:
            messages_data = []
            for message in results:
                message_id = message['id']
                details = service.get_message_details(message_id)
                messages_data.append({
                    'message_id': message_id,
                    'subject': details['headers']['subject'],
                    'from': details['headers']['from'],
                    'to': details['headers']['to'],
                    'date': details['headers']['date'],
                    'body': details['body'],
                })
            return messages_data
    except Exception as error:
        return f'Error: {error}'

def main():
    """Entry point para ejecutar el servidor MCP de Gmail."""
    mcp.run(transport='stdio')

import sys

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        raise

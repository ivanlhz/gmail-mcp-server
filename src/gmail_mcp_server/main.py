from mcp.server.fastmcp import FastMCP

from gmail.auth import authenticate_gmail
from gmail.models.label_model import GmailLabel, LabelColor
from gmail.service import GmailService

# Initialize FastMCP server
mcp = FastMCP("gmail-mcp-server")
api = authenticate_gmail()
service = GmailService(api)

@mcp.tool()
def get_labels():
    """Get labels from gmail"""
    try:
        return service.get_labels()
    except Exception as error:
        return f'Error: Getting labels.'

@mcp.tool()
def get_label_by_id(label_id: str):
    """Get a single label data from gmail using label id"""
    try:
        return service.get_label(label_id)
    except Exception as error:
        return f'Error Getting label: {error}.'

@mcp.tool()
def delete_label(label_id: str):
    """Delete a single label from gmail"""
    try:
        return service.delete_label(label_id)
    except Exception as error:
        return f'Error deleting label: {error}.'

@mcp.tool()
def create_label(name: str, bg_color: str = "#4a86e8", text_color: str = "#ffffff"):
    """Create label to gmail
    Allowed colors:
        "#000000", "#434343", "#666666", "#999999", "#cccccc", "#efefef", "#f3f3f3", "#ffffff",
        "#fb4c2f", "#ffad47", "#fad165", "#16a766", "#43d692", "#4a86e8", "#a479e2", "#f691b3",
        "#f6c5be", "#ffe6c7", "#fef1d1", "#b9e4d0", "#c6f3de", "#c9daf8", "#e4d7f5", "#fcdee8",
        "#efa093", "#ffd6a2", "#fce8b3", "#89d3b2", "#a0eac9", "#a4c2f4", "#d0bcf1", "#fbc8d9",
        "#e66550", "#ffbc6b", "#fcda83", "#44b984", "#68dfa9", "#6d9eeb", "#b694e8", "#f7a7c0",
        "#cc3a21", "#eaa041", "#f2c960", "#149e60", "#3dc789", "#3c78d8", "#8e63ce", "#e07798",
        "#ac2b16", "#cf8933", "#d5ae49", "#0b804b", "#2a9c68", "#285bac", "#653e9b", "#b65775",
        "#822111", "#a46a21", "#aa8831", "#076239", "#1a764d", "#1c4587", "#41236d", "#83334c",
        "#464646", "#e7e7e7", "#0d3472", "#b6cff5", "#0d3b44", "#98d7e4", "#3d188e", "#e3d7ff",
        "#711a36", "#fbd3e0", "#8a1c0a", "#f2b2a8", "#7a2e0b", "#ffc8af", "#7a4706", "#ffdeb5",
        "#594c05", "#fbe983", "#684e07", "#fdedc1", "#0b4f30", "#b3efd3", "#04502e", "#a2dcc1",
        "#c2c2c2", "#4986e7", "#2da2bb", "#b99aff", "#994a64", "#f691b2", "#ff7537", "#ffad46",
        "#662e37", "#ebdbde", "#cca6ac", "#094228", "#42d692", "#16a765"
    Args:
        name: label name
        bg_color: background color
        text_color: text color
    """
    try:
        label = GmailLabel(
            name=name,
            color=LabelColor(
                backgroundColor=bg_color,
                textColor=text_color
            )
        )

        return service.create_label(label)
    except Exception as error:
        return f'Error Creating label: {error}'

@mcp.tool()
def update_label(label_id: str, name: str, bg_color: str = "#4a86e8", text_color: str = "#ffffff"):
    """Update label to gmail
    Allowed colors:
        "#000000", "#434343", "#666666", "#999999", "#cccccc", "#efefef", "#f3f3f3", "#ffffff",
        "#fb4c2f", "#ffad47", "#fad165", "#16a766", "#43d692", "#4a86e8", "#a479e2", "#f691b3",
        "#f6c5be", "#ffe6c7", "#fef1d1", "#b9e4d0", "#c6f3de", "#c9daf8", "#e4d7f5", "#fcdee8",
        "#efa093", "#ffd6a2", "#fce8b3", "#89d3b2", "#a0eac9", "#a4c2f4", "#d0bcf1", "#fbc8d9",
        "#e66550", "#ffbc6b", "#fcda83", "#44b984", "#68dfa9", "#6d9eeb", "#b694e8", "#f7a7c0",
        "#cc3a21", "#eaa041", "#f2c960", "#149e60", "#3dc789", "#3c78d8", "#8e63ce", "#e07798",
        "#ac2b16", "#cf8933", "#d5ae49", "#0b804b", "#2a9c68", "#285bac", "#653e9b", "#b65775",
        "#822111", "#a46a21", "#aa8831", "#076239", "#1a764d", "#1c4587", "#41236d", "#83334c",
        "#464646", "#e7e7e7", "#0d3472", "#b6cff5", "#0d3b44", "#98d7e4", "#3d188e", "#e3d7ff",
        "#711a36", "#fbd3e0", "#8a1c0a", "#f2b2a8", "#7a2e0b", "#ffc8af", "#7a4706", "#ffdeb5",
        "#594c05", "#fbe983", "#684e07", "#fdedc1", "#0b4f30", "#b3efd3", "#04502e", "#a2dcc1",
        "#c2c2c2", "#4986e7", "#2da2bb", "#b99aff", "#994a64", "#f691b2", "#ff7537", "#ffad46",
        "#662e37", "#ebdbde", "#cca6ac", "#094228", "#42d692", "#16a765"
    Args:
        label_id: id of label to update
        name: label name
        bg_color: background color
        text_color: text color
    """
    try:
        label = GmailLabel(
            name=name,
            color=LabelColor(
                backgroundColor=bg_color,
                textColor=text_color
            )
        )

        return service.update_label(label_id, label)
    except Exception as error:
        return f'Error updating label: {error}'

@mcp.tool()
def get_emails_details(query: str):
    """Get emails details from gmail
    Args:
        query: gmail query string
    """
    try:
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

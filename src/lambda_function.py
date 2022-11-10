import json


def lambda_handler(event, context):
    headers = event.get('headers', 'no headers')
    ip_address = headers.get('x-forwarded-for', 'no IP')
    user_agent = headers.get('user-agent', json.dumps(headers))

    body = '<strong>\n'
    body += f"<p style=\"font-size: 72px\">{ip_address}</p>\n"
    body += '</strong><br />\n'
    body += f"{user_agent}<br />\n"

    return {
        'statusCode': 200,
        'body': body,
        "headers": {"Content-Type": "text/html"}
    }

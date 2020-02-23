import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formatdate
from datetime import datetime


def send_statistics(statistics: dict):

    email_server = os.getenv('EMAIL_SERVER')
    email_server_port = os.getenv('EMAIL_SERVER_PORT')

    mailbox = os.getenv('MAILBOX')
    mailbox_password = os.getenv('MAILBOX_PASSWORD')

    email_sender = os.getenv('EMAIL_SENDER')
    email_receivers = os.getenv('EMAIL_RECEIVERS').split('|')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Send mails
    with smtplib.SMTP_SSL(email_server, email_server_port, context=context) as server:

        server.login(mailbox, mailbox_password)

        # Send email
        msg = EmailMessage()
        msg.set_content(f"""
            Test statistics message
        """)
        msg.add_header('Subject', 'DB update statistics')
        msg.add_header('From', email_sender)
        msg.add_header('Date', formatdate(localtime=True))

        for receiver in email_receivers:
            server.sendmail(email_sender, receiver, msg.as_string())

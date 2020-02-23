import os
import smtplib
import ssl
from datetime import date

def send_statistics():

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
        msg = f"""
        From: {email_sender}
        Subject: DB update statistics
        Date: {date.today()}

        Test statistics message
        """
        
        for receiver in email_receivers:
            server.sendmail(email_sender, receiver, msg)

import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formatdate
from datetime import datetime

from jinja2 import Environment, PackageLoader, Template, select_autoescape


def send_summary(summary: dict):

    db = os.getenv("DB_FILE")
    date = formatdate(localtime=True)

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

        # Prepare and send end email
        msg = EmailMessage()
        msg.add_header('Subject', 'DB update summary')
        msg.add_header('From', email_sender)
        msg.add_header('Date', date)
        
        msg.set_content(_get_summary_content(db, date, summary))
        msg.set_type("text/html")


        for receiver in email_receivers:
            server.sendmail(email_sender, receiver, msg.as_string())


# Private helper methods

def _get_summary_content(db:str, date: str, summary: dict) -> str:
    jinja_env = Environment(
        loader=PackageLoader('utils','mail_templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = jinja_env.get_template('update_summary_mail.html')
    return template.render(db=db, date=date, summary_dict=summary)
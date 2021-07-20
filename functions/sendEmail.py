import smtplib
from credential import *


def send_email(recipient, subject, body):

    user_from = 'support@binaryvillage.com'
    user= username
    pwd= password
    FROM = user_from
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        return 'successfully sent the mail'
    except:
        return "failed to send mail"


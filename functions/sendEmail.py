from django.core.mail import send_mail

# ******************************************************************
# sent mail function
# *******************************************************************

def SendEmail(email_address,subject, message):
    from_email = "alok@binaryvillage.com"
    to_email = email_address

    send_mail(subject, message, from_email, [to_email], fail_silently=False,)

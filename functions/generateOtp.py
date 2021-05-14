import random
##from django.db import models
from userauth.models import *
################################
## Generate otp function
##############################

def GenerateOtp(email_address):
    try:
        data = EmailOtp.objects.get(email_address_id=email_address)
        print(data.counter)
        otp = (random.randrange(100000, 999999))
        EmailOtp.objects.filter(email_address_id=email_address).update(
            otp=otp,
            counter=data.counter+1
        )
        return otp
    except EmailOtp.DoesNotExist:
        otp = (random.randrange(100000, 999999))
        EmailOtp.objects.create(
            email_address_id=email_address,
            otp=otp,
            counter=1
        )
        return otp


def GenerateOtp(email_address):
    # return (random.randrange(100000, 999999))
    # check otp exists in the otp table or not
    try:
        data = EmailOtp.objects.get(email_address_id=email_address)
        print(data.counter)
        otp = (random.randrange(100000, 999999))
        EmailOtp.objects.filter(email_address_id=email_address).update(
            email_otp=otp,
            counter=data.counter+1
        )
        return otp
    except EmailOtp.DoesNotExist:
        # otp generated
        otp = (random.randrange(100000, 999999))
        # save otp to the otp table
        EmailOtp.objects.create(
            email_address_id=email_address,
            email_otp=otp,
            counter=1
        )
        return otp
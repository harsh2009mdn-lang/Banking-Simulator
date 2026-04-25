import random

def captcha():
    num=list(range(10))
    letters=list("abcdefghijklmnopqrstuvwxyz")
    cap=random.choices(num+letters,k=4)
    s=''
    for i in cap:
        s+=str(i)
        s+=" "
    return s

print(captcha())

def password():
    num=list(range(10))
    letters=list("abcdefghijklmnopqrstuvwxyz")
    pwd=random.choices(num+num+num+letters,k=5)
    s=''
    for i in pwd:
        s+=str(i)
        s+=""
    return s

print(password())

def close_otp():
    otp=random.randint(1000,9999)
    return otp

def forgot_otp():
    otp=random.randint(1000,9999)
    return otp
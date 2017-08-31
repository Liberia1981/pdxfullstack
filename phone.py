def phone_format(n):
    return n[0:3]+"-"+n[3:6]+'-'+n[6:]
phone=input("What is your number? ")
print(phone_format(phone))

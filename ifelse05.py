email = input("Emailingzni kiriting:")

if "@" in email:
    if email.endswith(".com") or email.endswith(".uz") or email.endswith(".net"):
        print ("Email qabul qilindi:")

else:
    print("email notug'ri formatda:")

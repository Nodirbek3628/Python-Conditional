ticket = 80

age = int(input("yoshingizni  kiriting:"))

if ticket < 7:
    ticket *= 0.5

if ticket >= 7 and ticket <= 17:
    ticket *= 0.2

if ticket > 60:
    ticket *= 0.3

print("bilet narxi",ticket)
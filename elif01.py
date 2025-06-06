number = int(input("Ballni kiriting:"))

if number >= 90 and number <= 100:
    print("A(A'lo)")
elif number >= 80 and number <= 89:
    print("B(Yaxshi)")
elif number >= 70 and number <= 79:
    print("D (Qoniqarsz)")
elif number >= 0 and number <59:
    print("F (Rad)")
elif number > 100:
    print("Ball 0-100 oralig'ida bolishi kerak.")


hour = int(input("Vaqtni kiriting:"))

if hour >= 5 and hour <= 11:
    print("Ertalab")

elif hour >= 18 and hour <= 21:
    print("Kechqurun:")

elif hour >= 22 and hour <= 24 or hour > 0 and hour < 5:
    print("Tun :")



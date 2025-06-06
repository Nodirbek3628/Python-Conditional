distance = int(input("Masofani kiriting (km): "))

if distance < 0:
    print("Masofa manfiy bo'la olmaydi: ")
elif distance >= 0 and distance <= 1:
    print("Piyoda yuring:")

elif distance > 1 and distance <= 5:
    print("Velosiped yoki elektr skutr: ")

elif distance > 5 and distance <= 50:
    print("Avtobus yoki mashina : ")
elif distance > 50:
    print("Poyezda yoki samaliyot: ")

money = 5000

maxsulot = int(input("Yechmoqchi bo'lgan summani kiriting:"))

if maxsulot < 0:
    print("Manfiy summa kiritib bo'lmaydi:")

if money > maxsulot and maxsulot > 0:
    money -= maxsulot
    print("Pul yechildi. Qolgan summa ",money,"sum")

else:
    print("Mablag' yetarli emas.Sizning balansingiz:",money,"Sum")

    

templete = "{number} soni {n} bo'linadi "

number = int(input("Sonni kiriting:"))

if number % 2 == 0:
    print(templete.format(number=number,n=2))
if number % 3 == 0:
    print(templete.format(number = number,n = 3))
if number % 5 == 0:
    print(templete.format(number = number,n = 5))
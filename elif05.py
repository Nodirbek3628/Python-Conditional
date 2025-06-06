weight = float(input("Vazningizni kiriting (kg) da:"))
tall = float(input("bo'yingizni kiriting (m) da:"))

BMI = weight/tall**2

if BMI < 18.5:
     tasnif = ("Kam vazn")

elif 18.5 <= BMI < 25:
    tasnif = ("Normal vazn")

elif 25 <= BMI < 30:
    tasnif = ("Ortiqcha vazn")

elif BMI >= 30:
    tasnif = ("Semizlik")

print(f"BMI: {BMI:.2f}")
print(f"Tasnif: {tasnif}")

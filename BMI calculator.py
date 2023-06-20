height = float(input("Please enter ur height(cm)\n"))
weight = float(input("Please enter ur weight(kg)\n"))

height /= 100
bmi = (weight/(height*height))

if bmi < 18.5:
    print(f"Your BMI is: {round(bmi ,1)} (Underweight)")
elif bmi < 24:
    print(f"Your BMI is: {round(bmi ,1)} (Normal Weight)")
elif bmi < 27:
    print(f"Your BMI is: {round(bmi ,1)} (Abit fat)")
elif bmi < 35:
    print(f"Your BMI is: {round(bmi ,1)} (Center fat)")
else:
    print(f"Your BMI is: {round(bmi ,1)} (Very fat)")


height = float(input("Please enter ur height(cm)\n"))
weight = float(input("Please enter ur weight(kg)\n"))

height /= 100
bmi = (weight/(height*height))

print(f"Your BMI is: {round(bmi ,1)}")

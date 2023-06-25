
def print_info():
    print("Hello")
    print("World")

print_info()

def print_name(name ,age):
    print(f"{name} is a good boy, is a {age} year old")

print_name("Ali" , 15)
print_name(age = 15 , name="ali")

def info(name ,age ,height ,weight):
    print(f"\n{name} this year is {age} year old")
    print(f"{name} height is {height}cm")
    print(f"{name} weight is {weight}kg")

info("Ali",15,140,35)
info("Bee",16,170,54)
info("Cat",17,180,75)

def find_max(num1 ,num2 ,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

find_max(1000, 400,-300)
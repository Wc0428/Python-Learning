print("Welcome to use ramen ordering machine~")
print("(1) Normal Ramen RM220")
print("(2) Soy Sauce Ramen RM240")
print("(3) Tonkotsu Ramen RM280")

order = input("Please choose a ramen (Enter:1 or 2 or 3)")
add_big = input("Want add bigger size, Tonkotsu Ramen+RM50 other Ramen is+RM30 (Enter:Y or N)")
add_egg = input("Want add on egg+RM30 (Enter:Y or N)")
add_pork = input("Want add on pork+RM30 (Enter:Y or N)")

bill = 0

if order == "1":
    bill += 220
elif order == "2":
    bill += 240
elif order == "3":
    bill += 280

if add_big =="Y":
    if order == "3":
        bill += 50
    else:
        bill += 30

if add_egg == "Y":
    bill += 30

if add_pork == "Y":
    bill += 30

if add_big == "Y" and add_egg =="Y" and add_pork == "Y":
            bill -= 20
            print(f"\n\nGet the discount RM20, Total Bill is RM{bill}, Thx for u coming")
else:
    print(f"\n\nYou total bill is RM{bill}, thx for u coming")


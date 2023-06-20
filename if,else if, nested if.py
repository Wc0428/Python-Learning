
score = 100
cheat = True

if score > 90:
    if cheat:
        print("No money")
    else:
        print("RM100")
elif score >= 80:
    print("RM80")
elif score > 70:
    print("RM50")
else:
    print("RM10")
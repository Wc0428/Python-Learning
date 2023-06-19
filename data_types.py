#string
print("I am \"21\" Year old")
print('I am \'21\' Year old')
print("I am '21' Year old")
print('I am "21" Year old')
print("HI My name is Luu Wei Chek\nI am 21 Year old")

age = 21
height = 180.5
is_male = True

print("Ali year old is 21,height is 180.5,is male : True")
# if like below this example will wrong
# print("Ali year old is"+ age +", height is"+ height+",is male : "+is_male)
#waste time method
print("Ali year old is "+ str(age) +",height is "+ str(height)+",is male : "+str(is_male))
#f-string ( save time method)
print(f"Ali year old is {age},height is {height},is male : {is_male}")


#int
# num1 = int(input("enter"))
#float
# num2 = float(input("enter"))
#boolean



# print(num1 + num2)
num = input("Please insert 2 digital number: ")
print(int(num[0])+int(num[1]))




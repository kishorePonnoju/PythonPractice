# print("hello "*5 + "4")

# Replace fileds
# age =24
# print("My age is {0} years".format(age))
# print("There are {0} days in {1} {2} {3}".format(31,"jan","Mar","May"))
# print("jan: {1} feb:{0} May:{1} Apr:{2}".format(28,31,30))

# formating string
# for i  in range (1,13):
#     print("No.{0:2} squared is {1:<3} and cube is {2:^4}".format(i,i**2,i**3))

# FStrings
# name= "Tim"
# age =24
# print(name + "is " + "{0} ".format(age) + "years")
# print(name + f"is {age} years")
# print(f"Pi is Approximately {22/7:12.50f}")

# print("%s is %d years" % (name,age))
# print(f"{name} is {age} years")

# print("*"*80)
# IF condition

# name =input("Please enter your name ")
# age = int(input("How old you,{0} ".format(name)))

# if age > 18 :
#     print("Old enough to vote")
# else:
#     print("please come back in {0} year".format(18-age))

# if elif else
# answer =5
# guess = int(input("Please guesss a number between 1 to 10 "))
# if guess < answer :
#     print("please guess the higher number")
# elif guess > answer :
#     print("Please guess the lower number")
# else:
#     print("COrrect guess")


# age = int(input("How old are you "))
# #if age >= 16 and age <=65:
# if 16<= age <=65 :
#     print("Have a good Day at work")

# day= "Sunday"
# temp = 30
# raining = False

# if day == "Sunday" and temp > 27 and not raining :
#     print("Go swiming")
# else:
# print("Learn python")

#not in
# activity = input("What would you like to to today? ")

# if "cinema" not in activity.casefold():
#     print("But I want to go the cinema")
# else:
#     print("Hurry lets go to the Cinema ! ")


# For loops
# parrot = "Norwegian Blue"

# for character in parrot:
#     print(character)

# number ="9,223;372:036 854,775;807"
# separators =""

# for char in number:
#     if not char.isnumeric():
#         separators +=char
# print(separators)

# value = "".join(char if char not in separators else " " for char in number ).split()
# print([int(val) for val in value])

number = input("Please enter a series of numbers,using any separators your like: ")
separators =""

for char in number:
    if not char.isnumeric():
        separators +=char
print(separators)

value = "".join(char if char not in separators else " " for char in number ).split()
print(value)
print([int(val) for val in value])
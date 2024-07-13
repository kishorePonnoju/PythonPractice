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

# number = input("Please enter a series of numbers,using any separators your like: ")
# separators =""

# for char in number:
#     if not char.isnumeric():
#         separators +=char
# print(separators)

# value = "".join(char if char not in separators else " " for char in number ).split()
# print(value)
# print([int(val) for val in value])

# panagram = """The qucik brown fox jumps over teh lazy dog"""

# words=panagram.spilt()
# print(words)


# Tuple

# t ="a","b","c"
# print(t)
# print()
# print(t)

# name = "Tim"
# age =10
# print(name,age,"python",20)
# print((name,age,"python",12))

# welcome = "Welcom to my Nightmae","Alice copper ",1975
# bad ="Company","Bad company ",1975
# budgie = "Night flight","Budgie",1976
# imelda = "More Mayhem", "Emilda May",2011
# Metallica = "Ride the lighting","Metallica",1985

# print(Metallica)
# print(Metallica[0])
# print(Metallica[1])
# print(Metallica[2])


# # Below line will throw an error
# # Metallica[0] ="Master of pupets"
# Metallica2 = list(Metallica)
# print(Metallica2)
# Metallica2[0] ="Master of pupets"
# print(Metallica2)

# so the final conclusion is that, tuple data can't be modified once it is defined.


# a = b = c = d = e = f = 42

# print(c)
# print()
# x,y,z = 1,2,4
# print (x,y,z)
# print("Unpacking the tuple")
# data= (1, 2, 76) # data represents a tuple
# x, y, z = data
# print(x)
# print(y)
# print(z)
# print("unpacking the list")
# data_list =[12,13,14]
# data_list.append(15)
# p,q,z= data_list
# print(p)
# print(q)
# print(z)

# enumerate exmple using tuple
# for index, character in enumerate("abcdefghijklmnopqrtsuvwxyz"):
#     print(index ,character,end=" ")

##################
# Nested tuple

# album = (
#          ("Welcom to my Nightmae","Alice copper ",1975),
#          ("Company","Bad company ",1975),
#          ("Night flight","Budgie",1976),
#          ("More Mayhem", "Emilda May",2011),
#          ("Ride the lighting","Metallica",1985)
#          )
# print(len(album))

# for album_inside in album:
#     for item in album_inside:
#         print(item,end="|")
#     print()

# for name,artist,year in album:
#     print(f"name ={name}  \t artist ={artist} \t year={year}")

# albums = [
#     ("Welcome to my Nightmare", "Alice Cooper", 1975,
#      [
#          (1, "Welcome to my Nightmare"),
#          (2, "Devil's Food"),
#          (3, "The Black Widow"),
#          (4, "Some Folks"),
#          (5, "Only Women Bleed"),
#      ]
#      ),
#     ("Bad Company", "Bad Company", 1974,
#      [
#          (1, "Can't Get Enough"),
#          (2, "Rock Steady"),
#          (3, "Ready for Love"),
#          (4, "Don't Let Me Down"),
#          (5, "Bad Company"),
#          (6, "The Way I Choose"),
#          (7, "Movin' On"),
#          (8, "Seagull"),
#      ]
#      ),
#     ("Nightflight", "Budgie", 1981,
#      [
#          (1, "I Turned to Stone"),
#          (2, "Keeping a Rendezvous"),
#          (3, "Reaper of the Glory"),
#          (4, "She Used Me Up"),
#      ]
#      ),
#     ("More Mayhem", "Imelda May", 2011,
#      [
#          (1, "Pulling the Rug"),
#          (2, "Psycho"),
#          (3, "Mayhem"),
#          (4, "Kentish Town Waltz"),
#      ]
#      ),
# ]

# for name, artist, year, songs in albums:
#     print("Album: {}, Artist: {}, Year: {}, Songs: {}"
#           .format(name, artist, year, songs))

# print()

# album = albums[2]
# print(album)

# songs = album[3]
# print(songs)

# song = songs[1]
# print(song)
# print(song[1])


# Function demo

# def noreturnfunction():
#     print("THis is not return any argument")

# def mutiply(a,b):
#     return a*b

# print(mutiply(4,5))
# noreturnfunction()

# Handling invalid Arugment
def banner_text(text):
    screen_width = 80
    if len(text) > (screen_width-4):
        raise ValueError(f"String {0} is larger then Specified width {1}".
                         format(text,screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width-4)
        output_string = f"**{0}**".format(centred_text)
        print(output_string)

banner_text("*")
banner_text("This is code sinnpet implemented By")
banner_text("Kishore Ponnoju")
banner_text("On 13-07-2024")
banner_text("To Explain the Banner")
banner_text("k"*100)
banner_text("*")





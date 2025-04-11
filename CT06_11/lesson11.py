#px = int(input("What is the price of this?"))
#if px <= 5:
#    print("Sounds good!")
#elif  px <= 50: 
#    print("Are you sure you need this?")
#elif px <= 500: 
#    print("Where are you getting this money from?!")
#else:
#    print("Don't even think about it!")

#rider1 = 125
#rider2 = 150
#if rider1 > 120 and rider2 > 120:
#    print ("you r allowed to ride")

#num1 = int(input("give me a number"))
#if num1 % 3 == 0 and num1 % 7 == 0 :
#    print ("The number is divisible by 3 and 7!") 

#rider1 = 25
#rider2 = 6
#if rider1 >= 18 or rider2 >= 18:
#    print ("you can ride")
#else:
#    print("you cannot ride")

#buyer = int(input("how old are you? ^__^ >:)"))
#if buyer < 12 or buyer > 65:
#    print (" your ticket price is $12. ^__^ >:)")
#else: 
#    print ("your ticket price is $20. ^__^ >:)")

#gender = input("to enter this SKIBIDI TOILET, Please enter your GEN_deR. enter M/Male if male gender")
#if gender == m or gender == male:

#colour = input("guess a colour")
#if not (colour == "green") :
#  print("try again")
#else:
#  print("correct")

#day = input("what day is it?")
#if not (day == "saturday"or"sunday"):
#  print ("it is the week end.yaaaaaay! ")
#else:
#  print("it is not the weekend end. booooo")

#burger = input("do you want a burger?")
#fries = input("do you want a fries?")
#drink = input("do you want a drink?")
#if burger == "yes" and fries == "yes" and not drink == "yes":
#  print ("won't u get thirsty?")
#else:
#  print("order submited.  -__-")

found_o = False
found_e = False

yes = 0
word = input("give me a 5 letter word")
for letter in word:
    if letter == "o":
        found_o = True
    if letter == "e":
        found_e = True
        
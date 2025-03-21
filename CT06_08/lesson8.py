#num1 = int(input("give me a number."))
#num2 = num1
#for char in range (4):
#    num1 = int(input("give me a number."))
#    num2 = num1 * num2
#print ("the total is " + str(num2))

import time

#for char in range(10,0,-1):
#    print (char)
#    time.sleep(1)
#print(time.time())

#num1 = input("what number do you want to count down from?")
#num1 = int(num1)
#for char in range(num1,0,-1):
#    print (char)
#    time.sleep(1)
#print(time.time())

import random

#num = random.randint(1,6)
#print(num)

#for char in range(1,21):
#    num = random.randint(0,9999)
#    print(str(char) + " generated " + str(num))

#num1 = random.randint(1,50)
#num2 = random.randint(1,50)
#num3 = num1 + num2
#num4 = input ("what is " + str(num1) + " + " + str(num2) + "?")
#num4 = int(num4)
#if num3 == num4:
#    print("correct")
#else:
#    print("incorrect")

#num1 = random.randint(1,50)
#start = int(input("give me a start number"))
#end = int(input("give me a end number"))
#if num1 >= start:
#    if num1 <= end:
#        print ("True")
#    else:
#        print("False")
#else:
#    print("False")

#num1 = random.randint(1,50)
#print ("random number is " + str(num1))
#start = int(input("start number?"))
#end = int(input("end number?"))
#print( start <= num1 <= end )

#num1 = int(input("give me a number? "))
#num1 = (num1 % 2)
#if num1 == 0 :
#    print ("True")
#else:
#    print ("False")

num1 = int(input("start number?"))
num2 = int(input("start number?"))
num3 = num1 % num2
if num3 == 0:
    print("True")
else:
    print("False")
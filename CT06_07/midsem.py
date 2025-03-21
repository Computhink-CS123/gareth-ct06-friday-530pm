#asking for the user's name 
#name = input("What is your name? ")
#giving the greeting
#print ("Nice to meet you," + str(name) + "!")




#asking for start number
num1 = input("Please give me a starting number?")
num1 = int(num1)
#asking for end number
num2 = input("Please give me a ending number?")
num2 = int(num2)
#asking for increment number
num3 = input("Please give me a increment number?")
num3 = int(num3)
#counting the numbers
for char in range(num1,num2,num3):
    print (char)
#num1 = input("give me a number")
#num2 = input("give me a number")
#num1 = int(num1)
#num2 = int(num2)
#if num1 > num2:
#    temp = num1
#    num1 = num2
#    num2 = temp

#for count in range(num1,num2):
#    print(count)

#numpupil = input("how many people are there in your class")
#numpupil = int(numpupil)
#tolscore = 0
#for count in range(numpupil):
#    score = input("what is the person's score?")
#    score = int(score)
#    tolscore = tolscore + score
#avescore = tolscore / numpupil
#print ("the average score is " + str(avescore))

#for i in range(3):
#    print("Hello, World!")

#for i in range(5):
#    print(i)

#print("Hello, World!")

#f = 5

#print ("Hello, World!")
#age = 1
#print(age)
#name = "Alice"
#print(name)
#x = 5
#print(x)
#print("Hello, World!")
#age = 25
#print(age + 1)
#number = 10
#print(number - 5)
#print("Repeat" * 3)
#year = 2023
#print("The year is " + str(year))
#x = 10
#y = x / 2
#end = 5
#for i in range(end):
#    print(i)


import random
hidden = random.randint(1,100)
#print("the hidden number is " , hidden)

print("i have a hidden number from 1 to 100")
print("guess my hidden number")

tries = 7
correct = False
for count in range(tries):
    reply = input("guess a number")
    reply = int(reply)
    if reply < hidden:
        print("guess a bigger number")
    elif reply > hidden:
        print ("guess a smaller number")
    else:
        print("you got it! the number is " , hidden)
        correct = True
        break
if not correct:
    print("you do not have any more tries left.YoU LoSe. The correct number is " , )
print("Game over")
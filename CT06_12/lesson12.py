#visitors = 0
#while visitors < 50:
#    visitors += 1
#    print(visitors)
#
#visitor1 = 18
#while visitor1 <30:
#    visitor1 += 1
#    print(visitor1)
#visitor2 = 4
#while visitor2 <25:
#     visitor2 += 1
#     print(visitor2)

#visitors = 0
#while visitors < 50:
#    print(visitors)
#    if visitors == 30:
#        break
#    visitors += 1

#order = ("")
#while True:
#    ans = input("what is your order?")
#    if ans == "end":
#        break

#counter = 0
#import random
#for char in range(10):
#    num1 = random.randint(10,20)
#    num2 = random.randint(1,10)
#    raneq = random.randint(1,3)
#        ans = input("what is " + str(num1) + " + " + str(num2) + "? ")
#        ans = int(ans)
#        truans = num1 + num2
#    elif raneq == 2:
#        ans = input("what is " + str(num1) + " - " + str(num2) + "? ")
#       ans = int(ans)
#        truans = num1 - num2
#    elif raneq == 3:
#        ans = input("what is " + str(num1) + " x " + str(num2) + "? ")
#        ans = int(ans)
#        truans = num1 * num2
#    if not ans == truans:
#        print ("wrong")
#    else :
#        print ("correct")
#        counter = counter + 1
#print (counter)

import random
num = 0
while True:
    num = random.randint(1,6)
    print (num)
    if not num == 4:
        print ("i want four! >:(")
    else:
        print ("yay!we have a four!:)")
        break

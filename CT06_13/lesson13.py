#cash = 1000
#while True:
#    ask = input("for (withdraw, press 1), (deposit, press 2), (check balance, press 3), (exit, press 4) ")
#    if ask == "3":
##        print ("your balance is $" , cash)
#    elif ask == "4":
#        print ("thank you!")
#        break
#    elif ask == "1":
#        draw = int(input("how much money would you like to withdraw? "))
#        if draw <= cash:
#            cash = cash - draw
#            print("here is your money")
#        else:
#            print("Err0r!Insufision balance!")
#    elif ask == "2":
#        depo = int(input("how much money would you like to deposit?"))
#        cash = cash + depo


groceries = ["Apples", "Bread","Carrots","Dates","Eggs","Flour","Grapes","Honey"]
#print(groceries)
#groceries[7] = "herbs"
#print(groceries)
#groceries.append("ice")
#groceries.insert(1,"banana")
#print (groceries)
#create a list with "name" = ["",""]
#to change a name list:"list name"[no.] = "name"
#to insert a name into list:"list name".insert(no.,"name")
#to take out a name in a list :"list name".pop(no.)

for a in groceries:
    if a == "Apples":
        print(str(a) + ": I need 5 of these")
    elif a == "Carrots":
        print(str(a) + ": I need 3 of these")
    elif a == "Grapes":
        print(str(a) + ": Get the FarmFresh brand")
    

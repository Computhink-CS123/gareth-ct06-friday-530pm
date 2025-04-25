cash = 1000
while True:
    ask = input("for (withdraw, press 1), (deposit, press 2), (check balance, press 3), (exit, press 4) ")
    if ask == "3":
        print ("your balance is $" , cash)
    elif ask == "4":
        print ("thank you!")
        break
    elif ask == "1":
        draw = float
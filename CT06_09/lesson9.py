#numapple = int(input("How many apples did you buy? "))
#numorange = int(input("How many oranges did you buy? "))
#if numapple > 5:
#    appleprice = numapple * 0.6 * 0.9
#else:
#    appleprice = numapple * 0.6
#
#if numorange > 5:
#    orangeprice = numorange * 0.9 * 0.9
#else:
#    orangeprice = numorange * 0.9
#totalprice = orangeprice + appleprice
#print (totalprice)

#positive_days = 0
#for char in range(7):
#    daytem = int(input("what is the tempreture for today? "))
#    if daytem > 30:
#        positive_days = positive_days + 1
#print (positive_days)

desirable = 0
undesirable = 0
for char in range(10):
    ratings = int(input("how much do u rate between 1 to 5? "))
    if ratings > 3:
        desirable = desirable + 1
    else:
        undesirable = undesirable + 1
print ("desirable ratings are:" , desirable , "undesirable ratings are")
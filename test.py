#Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here
#num = 10
#while num < 201:
#    print(num)
#    num = num + 10




###################################################

# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# Write your code here
#password = "superpass123"
#ans = input("enter the password")
#if password == ans:
#    print ("Access Granted")
#else:
#    print("Access Denied")







##########################################



# Basic List Functions
# Do the following operations to the list provided below
# Write the code below each question.

planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]

# 1. Write code below to print the 3rd item 
#    in this list using index e.g. earth
print(planets[2])

# 2. Write code to append neptune to this list.
planets.append("neptune")



# 3. Elon Musk has conquered Mars. 
#    Rename Mars in the list to be "muskworld"
planets[3]="muskworld"

# 4. Remove uranus from this list.
planets.pop(6)

# 5. Using a for loop, print all the planets 
#    from this list one by one.
for char in planets:
    print(char)


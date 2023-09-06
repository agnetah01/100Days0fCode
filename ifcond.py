 #first instance
x = 5
y = 10

if x > 0:
    print("x is positive")
    if y > 0:
        print("y is positive")
    else:
        print("y is not positive")
else:
    print("x is not positive")
    
    #second instance
age = 25
income = 50000

if age >= 18:
    if income >= 30000:
        print("You are eligible for a loan!")
    else:
        print("Sorry, your income is not sufficient for a loan.")
else:
    print("Sorry, you must be at least 18 years old to apply for a loan.")

#third instance
x = 10
y = 5

if x > 0:
    if y > 0:
        print("Both x and y are positive")
    elif y < 0:
        print("x is positive, but y is negative")
    else:
        print("x is positive, but y is zero")
else:
    if y > 0:
        print("x is zero, but y is positive")
    elif y < 0:
        print(" x and y are negative")
    else:
        print(" x and y are zero")
        
#fourth instance
x = 15

if x > 0 and x % 2 == 0:
    print("The number is positive and even")
elif x > 0 and x % 2 != 0:
    print("The number is positive and odd")
elif x < 0:
    print("The number is negative")
else:
    print("The number is zero")
        
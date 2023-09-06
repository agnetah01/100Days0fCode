#first instance
age = 25
income = 45000
credit_score = 700

if age >= 18:
    if income >= 30000:
        if credit_score >= 650:
            print("Congratulations! You are eligible for a low-interest loan.")
        elif credit_score >= 600:
            print("You are eligible for a loan, but the interest rate may be higher.")
        else:
            print("Sorry, your credit score is too low for a loan.")
    else:
        print("Sorry, your income is not sufficient for a loan.")
else:
     print("Sorry, you must be at least 18 years old to apply for a loan.")
     
#second instance
#Shopping Discounts:

total_amount = 150
is_member = True
has_coupon = True

if total_amount >= 100:
    if is_member:
        if has_coupon:
            print("Congratulations! You qualify for a 20% discount with the coupon.")
        else:
            print("Sorry, you need a coupon to avail the discount.")
    else:
        print("Sorry, the discount is only available for members.")
else:
    print("Sorry, the total amount must be at least 100 to qualify for a discount.")

#third instnce
#travel desitination rec
is_summer = True
budget = 5000
is_adventurous = True

if is_summer:
    if budget >= 5000:
        if is_adventurous:
            print("You should consider going on a thrilling adventure to Costa Rica!")
        else:
            print("How about a relaxing beach vacation in Bali?")
    else:
        print("Sorry, your budget is not sufficient for a summer vacation.")
else:
    print("If it's not summer, how about exploring the historic streets of Rome?")
    
#fourth instance
#job application screening
years_of_experience = 5
is_qualified = True
has_degree = True

if years_of_experience >= 3:
    if is_qualified:
        if has_degree:
            print("Congratulations! You have been shortlisted for an interview.")
        else:
            print("Sorry, a degree is required for this position.")
    else:
        print("Sorry, you do not meet the qualifications for this job.")
else:
    print("Sorry, you need at least 3 years of experience for this position.")

#fifth instance
#restaurant reservation
num_of_guests = 6
is_vegetarian = True
has_reservation = True

if num_of_guests <= 10:
    if is_vegetarian:
        if has_reservation:
            print("Your table is ready! Enjoy your meal at our vegetarian-friendly restaurant.")
        else:
            print("Sorry, a reservation is required to dine at our restaurant.")
    else:
        print("We apologize, but our restaurant only serves vegetarian dishes.")
else:
    print("Sorry, we can only accommodate up to 10 guests at a time.")
    
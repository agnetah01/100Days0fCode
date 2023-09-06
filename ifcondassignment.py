#using if else to decide shopping budget
budget = 1000
item_price = 250

if item_price <= budget:
    num_items = budget // item_price
    print("You can buy", num_items, "items with your budget!")
else:
    print("Oops, the item is too expensive for your budget. Save up some more!")
    
#using if else to decide factors that influence my career
interest = "passion"
salary = 50000
location = "urban"

if interest == "passion":
    if salary >= 50000:
        if location == "urban":
            print("youre on the right track.")
        else:
            print("its not worth it hun.")
    else:
        if location == "urban":
         print("great its close to home")
else:
    print("Too far")
    
#finding gift for someone
action = "helped me move"
gift = ""

if action == "helped me move":
    gift = "a gift card to their favorite restaurant."
elif action == "organized a surprise party":
    gift = "gift related to their hobbies or interests."
elif action == "achieved a personal goal":
    gift = "a gift that celebrates their accomplishment."
else:
    gift = "It depends on their interests. Consider something meaningful or personalized."

print("For their impressive action, I suggest giving them:", gift)
    
#using if elif else statements to decie what to buy for dinner with 1500
budget = 1500
dinner_choice = "spaghetti"
total_cost = 0

if dinner_choice == "spaghetti":
    spaghetti_cost = 300
    total_cost += spaghetti_cost
elif dinner_choice == "grilled chicken":
    chicken_cost = 500
    total_cost += chicken_cost
elif dinner_choice == "vegetable stir-fry":
    stir_fry_cost = 400
    total_cost += stir_fry_cost
else:
    print("Sorry, that option is not available.")

remaining_budget = budget - total_cost

if remaining_budget >= 0:
    print("You can afford", dinner_choice, "for dinner! Enjoy your meal!")
    print("You will have", remaining_budget, "left in your budget.")
else:
   print("Oops! budget is not enough for", dinner_choice)
print("Consider choosing a more budget-friendly option.")

#if elif else to decide to go to movies or sports event
budget = 1000
movie_ticket= 200
sport_event_ticket= 500

if budget >= sport_event_ticket:
    print("You have enough budget to attend a sports event!")
elif budget >= movie_ticket:
    print("You have enough budget to go for a movie!")
else:
    print("Oops!  budget is not enough for either option.")
    print("Consider choosing a more budget-friendly activity.")
    
#if elif else to perform errands
bank_errand = True
mini_activities = True

if bank_errand:
    print("I'll go to the bank to run the errand.")
    # Perform the bank errand

if mini_activities:
    print("After the bank errand, I can do some mini-activities.")
    # Perform the mini-activities

if not bank_errand and not mini_activities:
    print("If there's no bank errand or mini-activities, I can relax or do something else.")
    # Relax or do something else 
 
 #if elif else shopping budget
shopping_budget = 35000

if shopping_budget >= 20000:
    print("buy a new school bag and a pair of shoes.")
elif shopping_budget >= 10000:
    print("buy a new school bag and some school supplies.")
elif shopping_budget >= 5000:
    print("buy some school supplies and a lunchbox.")
else:
    print("buy some essential school supplies.")
    
#event on 29th aug
event_date = "29th August"

if event_date == "29th August":
    print("for 29th,start with a welcome speech and introductions.")
elif event_date == "30th August":
    print("for 30th, we can begin with a keynote address.")
else:
    print("For any other date, we can have a variety of activities like workshops and performances.")
    
#pack 3 things for trip
items_to_pack = ["clothes", "toiletries", "phone charger", "snacks"]

packed_items = []

for item in items_to_pack:
    if len(packed_items) >= 3:
        break
    else:
        packed_items.append(item)
else:
    packed_items.append("extra item")

print("I packed the following items for my trip:")
for item in packed_items:
    print(item)
    
#host guests
guests = 10
utensils_needed = []

for guest in range(1, guests + 1):
    if guest <= 2:
        utensils_needed.append("knife and fork")
    else:
        utensils_needed.append("spoon")

print("To make your event happen, you will need to buy the following utensils:")
for utensil in utensils_needed:
    print(utensil)
    
#manegerial tasks with team 
tasks = ["task1", "task2", "task3"]
team = ["member1", "member2", "member3"]

for task in tasks:
    for member in team:
        print(f"Assigning {task} to {member}")

print("All tasks have been assigned to the team.")
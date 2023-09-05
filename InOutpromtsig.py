#python code that prompts user to create a shopping list and calculate cost
shop_list={}
while True:
    item=input("enter shopping items:")
    if item.lower()=='done':
        break
    
price=float(input("enter price:"))
shop_list[item]=price
total_cost=sum(shop_list.values())
print("your shopping list:")
print(f"-{item}:{price}")
print(f"total cost:{total_cost}")


 




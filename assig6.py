#code that proomts user to enter name and card infonand check whether its a string or an integer
name=input("enter your name:")
card_no=input("enter your card number:")
if name.isdigit() or card_no.isdigit():
    print("the input is an integer")
else:
    print("the input is a string")

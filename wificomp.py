#In Python, argparse is a module used to parse command-line arguments in a script.
#It provides an easy and intuitive way to create command-line interfaces for Python programs

from argparse import Action
import datetime
from random import randint

class InternetConnection:
    def __init__(self, house_id, is_connected=True, last_payment_date=None):
        self.house_id = house_id
        self.is_connected = is_connected
        self.last_payment_date = last_payment_date
#make_payment Method:
#Simulates a payment by setting the is_connected attribute to True and updating the last_payment_date to the current date
    def make_payment(self):
        self.last_payment_date = datetime.date.today()
        self.is_connected = True

    def check_connection_status(self):
        if self.is_connected:
            print(f"House {self.house_id} is connected.")
        else:
            print(f"House {self.house_id} is disconnected. Please make a payment.")

def simulate_internet_connections():
    # Simulate a list of houses with internet connections
    houses = [InternetConnection(house_id) for house_id in range(1, 11)]

    # Simulate random disconnections for testing
    for house in houses:
        if randint(0, 1) == 0:
            house.is_connected = False

    return houses
#User Interaction:
#Users can simulate making payments for their houses and check the connection status
def main():
    houses=simulate_internet_connections()
    while True:
        print("\n1. Make a payment")
        print("2. Check connection status")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            house_id = int(input("Enter your house ID: "))
            house = houses[house_id - 1]

            if house.is_connected:
                print(f"House {house_id} is already connected.")
            else:
                house.make_payment()
                print(f"Payment successful. House {house_id} is now connected.")

        elif choice == '2':
            house_id = int(input("Enter your house ID: "))
            house = houses[house_id - 1]
            house.check_connection_status()

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
#In a real-world application, you would need to integrate a secure payment system,
#use Action database for storing information, and implement additional features for a complete solution.
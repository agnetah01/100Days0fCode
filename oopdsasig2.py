class User:
    def __init__(self, user_id, username, email, preferences):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.preferences = preferences

    def __str__(self):
        return f"User ID: {self.user_id}\nUsername: {self.username}\nEmail: {self.email}\nPreferences: {self.preferences}"

# Create user objects
user1 = User(1, "chase", "chasebakari@email.com", ["3-bedroom", "Pet-friendly"])
user2 = User(2, "syvester", "sylvestermumbi@email.com", ["2-bedroom", "Near schools"])
user3 = User(3, "newton", "newtonkarimi@email.com", ["4-bedroom", "With pool and gym"])

# Store user objects in a list
user_base = [user1, user2, user3]

# Print user information
for user in user_base:
    print(user)
    print("---------------------")

#question number2
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = None  # You can add timestamp logic here

class CommunicationManager:
    def __init__(self):
        self.users = {}
        self.messages = []

    def register_user(self, user):
        self.users[user.user_id] = user

    def send_message(self, sender_id, receiver_id, content):
        if sender_id not in self.users or receiver_id not in self.users:
            return "Invalid sender or receiver ID"

        sender = self.users[sender_id]
        receiver = self.users[receiver_id]

        message = Message(sender, receiver, content)
        self.messages.append(message)
        return "Message sent successfully"

    def get_messages_for_user(self, user_id):
        if user_id not in self.users:
            return "Invalid user ID"

        user_messages = []
        for message in self.messages:
            if message.receiver.user_id == user_id:
                user_messages.append(message)
        return user_messages

# Example usage:

# Create users
user1 = User(1, "brice", "briceyun@email.com")
user2 = User(2, "florence", "florencepugh@email.com")

# Create a communication manager
comm_manager = CommunicationManager()

# Register users with the communication manager
comm_manager.register_user(user1)
comm_manager.register_user(user2)

# Send a message
message_status = comm_manager.send_message(1, 2, "Hello, how can I help you?")
print(message_status)

# Retrieve messages for a user
user2_messages = comm_manager.get_messages_for_user(2)
for message in user2_messages:
    print(f"From: {message.sender.username}\nMessage: {message.content}")
    
#question3
   
import math

class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Pyramid(Triangle):
    def __init__(self, base, height, side1, side2, side3, slant_height):
        super().__init__(base, height, side1, side2, side3)
        self.slant_height = slant_height

    def calculate_volume(self):
        base_area = super().calculate_area()
        return (1/3) * base_area * self.height

    def calculate_surface_area(self):
        base_perimeter = super().calculate_perimeter()
        base_area = super().calculate_area()
        return (0.5 * base_perimeter * self.slant_height) + base_area

# Getting user input for triangle and pyramid parameters
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the length of side 1 of the triangle: "))
side2 = float(input("Enter the length of side 2 of the triangle: "))
side3 = float(input("Enter the length of side 3 of the triangle: "))
slant_height = float(input("Enter the slant height of the pyramid: "))

# Create object
pyramid = Pyramid(base, height, side1, side2, side3, slant_height)

# Calculate and display results
print(f"Triangle Area: {pyramid.calculate_area()}")
print(f"Triangle Perimeter: {pyramid.calculate_perimeter()}")
print(f"Pyramid Volume: {pyramid.calculate_volume()}")
print(f"Pyramid Surface Area: {pyramid.calculate_surface_area()}")


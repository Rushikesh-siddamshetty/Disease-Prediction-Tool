import uuid

class FoodOrderingChatbot:
    def __init__(self):
        self.menu = {
            "Pizza": 10.99,
            "Burger": 5.99,
            "Sushi": 8.99,
            "Pasta": 7.99
        }
        self.sessions = {}

    def start_session(self, user_id):
        self.sessions[user_id] = {"order": {}}
        return f"Welcome to Foodies, user {user_id}! How can I help you today?"

    def end_session(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]
            return "Thank you for visiting Foodies. Have a great day!"
        else:
            return "No active session found."

    def show_menu(self):
        menu_str = "Here's our menu:\n"
        for item, price in self.menu.items():
            menu_str += f"{item}: ${price:.2f}\n"
        return menu_str

    def select_item(self, user_id, item, quantity):
        if user_id not in self.sessions:
            return "Please start a session first."
        
        # Standardize the item name to match the keys in the menu
        item = item.title()
        
        if item in self.menu:
            order = self.sessions[user_id]["order"]
            order[item] = order.get(item, 0) + quantity
            return f"{quantity} {item}(s) added to your order."
        else:
            return "Sorry, we don't have that item."

    def show_order(self, user_id):
        if user_id not in self.sessions:
            return "Please start a session first."
        order = self.sessions[user_id]["order"]
        if not order:
            return "Your order is empty."
        order_str = "Your order summary:\n"
        total = 0
        for item, quantity in order.items():
            price = self.menu[item] * quantity
            order_str += f"{item}: {quantity} x ${self.menu[item]:.2f} = ${price:.2f}\n"
            total += price
        order_str += f"Total: ${total:.2f}"
        return order_str

    def process_payment(self, user_id, payment_method):
        if user_id not in self.sessions:
            return "Please start a session first."
        if payment_method not in ["credit_card", "paypal", "cash"]:
            return "Invalid payment method. Please choose 'credit_card', 'paypal', or 'cash'."
        
        order = self.sessions[user_id]["order"]
        if not order:
            return "Your order is empty. Add items to your order before making a payment."

        order_total = sum(self.menu[item] * quantity for item, quantity in order.items())
        payment_confirmation = f"Payment of ${order_total:.2f} via {payment_method} is successful."
        return payment_confirmation

    def confirm_order(self, user_id):
        if user_id not in self.sessions:
            return "Please start a session first."
        
        order = self.sessions[user_id]["order"]
        if not order:
            return "You have no items in your order to confirm."
        
        confirmation = "Thank you for your order! Your food will be delivered shortly."
        self.end_session(user_id)
        return confirmation

def main():
    chatbot = FoodOrderingChatbot()
    user_id = str(uuid.uuid4())  # Generate a unique user ID
    
    print(chatbot.start_session(user_id))
    
    while True:
        command = input("Enter command (menu, add, show, pay, confirm, quit): ").strip().lower()
        
        if command == "menu":
            print(chatbot.show_menu())
        elif command == "add":
            item = input("Enter item name: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            print(chatbot.select_item(user_id, item, quantity))
        elif command == "show":
            print(chatbot.show_order(user_id))
        elif command == "pay":
            payment_method = input("Enter payment method (credit_card, paypal, cash): ").strip().lower()
            print(chatbot.process_payment(user_id, payment_method))
        elif command == "confirm":
            print(chatbot.confirm_order(user_id))
        elif command == "quit":
            print(chatbot.end_session(user_id))
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

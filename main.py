import json
import os
import uuid #Universally Unique Identifier - 128 bit number
from datetime import datetime
from typing import Dict, List

# Single Responsibility: Manages JSON file operations
class JSONHandler:
    @staticmethod
    def initialize_json_files():
        # Initialize products.json
        if not os.path.exists('products.json'):
            products = {
                1: 'potato', 2: 'tomato', 3: 'bread', 4: 'butter',
                5: 'ketchup', 6: 'milk', 7: 'Jam', 8: 'CashewNuts',
                9: 'Sweet-kalakand', 10: 'kiwi'
            }
            with open('products.json', 'w') as file:
                json.dump(products, file, indent=4)

        # Initialize pricing.json
        if not os.path.exists('pricing.json'):
            pricing = {
                1: 2.0,   # potato: ₹2.0
                2: 1.5,   # tomato: ₹1.5
                3: 3.0,
                4: 4.0,
                5: 4.5,
                6: 3.65,
                7: 5.8,
                8: 13.8,
                9: 190.0,
                10: 34.8
            }
            with open('pricing.json', 'w') as file:
                json.dump(pricing, file, indent=4)

        # Initialize transactions.json
        if not os.path.exists('transactions.json'):
            with open('transactions.json', 'w') as file:
                json.dump([], file, indent=4)

        # Initialize feedback.json
        if not os.path.exists('feedback.json'):
            with open('feedback.json', 'w') as file:
                json.dump([], file, indent=4)

    @staticmethod
    def read_products() -> Dict[int, str]:
        with open('products.json', 'r') as file:
            products = json.load(file)
        return {int(k): v for k, v in products.items()}

    @staticmethod
    def read_pricing() -> Dict[int, float]:
        with open('pricing.json', 'r') as file:
            pricing = json.load(file)
        return {int(k): float(v) for k, v in pricing.items()}

    @staticmethod
    def save_transaction(transaction_id: str, items: Dict[int, int], total: float):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction = {
            'transaction_id': transaction_id,
            'items': items,
            'total': total,
            'timestamp': timestamp
        }
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        transactions.append(transaction)
        with open('transactions.json', 'w') as file:
            json.dump(transactions, file, indent=4)

    @staticmethod
    def save_feedback(transaction_id: str, feedback: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        feedback_entry = {
            'transaction_id': transaction_id,
            'feedback': feedback,
            'timestamp': timestamp
        }
        with open('feedback.json', 'r') as file:
            feedbacks = json.load(file)
        feedbacks.append(feedback_entry)
        with open('feedback.json', 'w') as file:
            json.dump(feedbacks, file, indent=4)

    @staticmethod
    def display_json_contents():
        print("\n=== Displaying JSON File Contents ===")

        # Display products.json
        print("\nProducts (products.json):")
        print(f"{'Product ID':<12} {'Name':<20}")
        print("-" * 32)
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
                for pid, name in products.items():
                    print(f"{pid:<12} {name:<20}")
        except FileNotFoundError:
            print("products.json not found.")

        # Display pricing.json
        print("\nPricing (pricing.json):")
        print(f"{'Product ID':<12} {'Price (₹)':<10}")
        print("-" * 22)
        try:
            with open('pricing.json', 'r') as file:
                pricing = json.load(file)
                for pid, price in pricing.items():
                    print(f"{pid:<12} ₹{float(price):<9.2f}")
        except FileNotFoundError:
            print("pricing.json not found.")

        # Display transactions.json
        print("\nTransactions (transactions.json):")
        print(f"{'Transaction ID':<36} {'Items':<30} {'Total (₹)':<12} {'Timestamp':<20}")
        print("-" * 98)
        try:
            with open('transactions.json', 'r') as file:
                transactions = json.load(file)
                for t in transactions:
                    items_str = ';'.join([f"{k}:{v}" for k, v in t['items'].items()])
                    print(f"{t['transaction_id']:<36} {items_str:<30} ₹{t['total']:<11.2f} {t['timestamp']:<20}")
        except FileNotFoundError:
            print("transactions.json not found.")

        # Display feedback.json
        print("\nFeedback (feedback.json):")
        print(f"{'Transaction ID':<36} {'Feedback':<30} {'Timestamp':<20}")
        print("-" * 86)
        try:
            with open('feedback.json', 'r') as file:
                feedbacks = json.load(file)
                for f in feedbacks:
                    print(f"{f['transaction_id']:<36} {f['feedback']:<30} {f['timestamp']:<20}")
        except FileNotFoundError:
            print("feedback.json not found.")
        print("\n=== End of JSON Contents ===\n")

# Single Responsibility: Manages cart operations
class Cart:
    def __init__(self):
        self.items: Dict[int, int] = {}  # product_id: quantity
        self.saved_for_later: Dict[int, int] = {}  # product_id: quantity for saved items

    def add_item(self, product_id: int, quantity: int, products: Dict[int, str]) -> bool:
        if product_id not in products:
            print(f"Product ID {product_id} does not exist.")
            return False
        self.items[product_id] = self.items.get(product_id, 0) + quantity
        return True

    def update_item(self, product_id: int, quantity: int, products: Dict[int, str]) -> bool:
        if product_id not in products:
            print(f"Product ID {product_id} does not exist.")
            return False
        if quantity <= 0:
            self.remove_item(product_id)
        else:
            self.items[product_id] = quantity
        return True

    def remove_item(self, product_id: int):
        if product_id in self.items:
            del self.items[product_id]

    def save_for_later(self, product_id: int, quantity: int, products: Dict[int, str]) -> bool:
        if product_id not in products:
            print(f"Product ID {product_id} does not exist.")
            return False
        if product_id in self.items:
            available_quantity = self.items[product_id]
            if quantity > available_quantity:
                print(f"Cannot save {quantity} of {products.get(product_id, 'Unknown')}. Only {available_quantity} in cart.")
                return False
            self.saved_for_later[product_id] = self.saved_for_later.get(product_id, 0) + quantity
            remaining_quantity = available_quantity - quantity
            if remaining_quantity > 0:
                self.items[product_id] = remaining_quantity
            else:
                del self.items[product_id]
            return True
        print(f"Product ID {product_id} is not in the cart.")
        return False

    def move_to_cart(self, product_id: int, quantity: int, products: Dict[int, str]) -> bool:
        if product_id not in products:
            print(f"Product ID {product_id} does not exist.")
            return False
        if product_id in self.saved_for_later:
            available_quantity = self.saved_for_later[product_id]
            if quantity > available_quantity:
                print(f"Cannot move {quantity} of {products.get(product_id, 'Unknown')}. Only {available_quantity} available in saved-for-later.")
                return False
            self.items[product_id] = self.items.get(product_id, 0) + quantity
            remaining_quantity = available_quantity - quantity
            if remaining_quantity > 0:
                self.saved_for_later[product_id] = remaining_quantity
            else:
                del self.saved_for_later[product_id]
            return True
        print(f"Product ID {product_id} is not in saved-for-later list.")
        return False

    def view_saved_items(self, products: Dict[int, str]):
        if not self.saved_for_later:
            print("No items saved for later.")
            return
        print(f"\n{'Saved Items':<20} {'Quantity':<10}")
        print("-" * 30)
        for product_id, quantity in self.saved_for_later.items():
            item_name = products.get(product_id, "Unknown")
            print(f"{item_name:<20} {quantity:<10}")

    def get_total(self, pricing: Dict[int, float]) -> float:
        total = 0.0
        for product_id, quantity in self.items.items():
            total += pricing.get(product_id, 0.0) * quantity
        return total

# Single Responsibility: Handles invoice generation
class InvoiceGenerator:
    @staticmethod
    def generate_invoice(transaction_id: str, cart: Cart, products: Dict[int, str], pricing: Dict[int, float]):
        print(f"\nINVOICE")
        print(f"Transaction ID: {transaction_id}")
        print(f"{'ITEM':<20} {'QUANTITY':<10} {'PRICE':<10} {'TOTAL':<10}")
        print("-" * 50)
        total = 0.0
        for product_id, quantity in cart.items.items():
            item_name = products.get(product_id, "Unknown")
            price = pricing.get(product_id, 0.0)
            item_total = price * quantity
            total += item_total
            print(f"{item_name:<20} {quantity:<10} ₹{price:<9.2f} ₹{item_total:.2f}")
        print("-" * 50)
        print(f"Total: ₹{total:.2f}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Single Responsibility: Handles payment processing
class PaymentProcessor:
    @staticmethod
    def process_payment(cart: Cart, pricing: Dict[int, float]) -> float:
        return cart.get_total(pricing)

# Single Responsibility: Manages feedback
class FeedbackManager:
    @staticmethod
    def collect_feedback(transaction_id: str):
        choice = input("Do you want to provide feedback? (yes/no): ").strip().lower()
        if choice == 'yes':
            feedback = input("Please enter your feedback: ").strip()
            JSONHandler.save_feedback(transaction_id, feedback)
            print("Feedback saved successfully!")
        else:
            print("No feedback provided.")

# Open/Closed: Main app class orchestrates the workflow
class GroceryApp:
    def __init__(self):
        self.cart = Cart()
        self.transaction_id = str(uuid.uuid4())
        JSONHandler.initialize_json_files()
        self.products = JSONHandler.read_products()
        self.pricing = JSONHandler.read_pricing()

    def start(self):
        print("Welcome to the Grocery App!")
        print("Available products:")
        for pid, name in self.products.items():
            print(f"{pid}: {name} (₹{self.pricing.get(pid, 0.0):.2f})")

        while True:
            action = input("\nEnter action (add/update/remove/save/move/view/done): ").strip().lower()
            if action == 'done':
                if self.cart.items:
                    total = self.cart.get_total(self.pricing)
                    JSONHandler.save_transaction(self.transaction_id, self.cart.items, total)
                    InvoiceGenerator.generate_invoice(self.transaction_id, self.cart, self.products, self.pricing)
                    FeedbackManager.collect_feedback(self.transaction_id)
                    JSONHandler.display_json_contents()
                    print("Transaction completed. Exiting...")
                else:
                    print("Cart is empty. Exiting without saving transaction.")
                    JSONHandler.display_json_contents()
                break
            elif action == 'add':
                self._handle_add()
            elif action == 'update':
                self._handle_update()
            elif action == 'remove':
                self._handle_remove()
            elif action == 'save':
                self._handle_save_for_later()
            elif action == 'move':
                self._handle_move_to_cart()
            elif action == 'view':
                self.cart.view_saved_items(self.products)
            else:
                print("Invalid action. Please try again.")

    def _handle_add(self):
        try:
            product_id, quantity = map(int, input("Enter product_id,quantity (e.g., 1,12): ").split(','))
            if self.cart.add_item(product_id, quantity, self.products):
                print(f"Added {quantity} of {self.products.get(product_id, 'Unknown')} to cart.")
        except ValueError:
            print("Invalid input. Use format: product_id,quantity")

    def _handle_update(self):
        try:
            product_id, quantity = map(int, input("Enter product_id,quantity (e.g., 2,6): ").split(','))
            if self.cart.update_item(product_id, quantity, self.products):
                print(f"Updated {self.products.get(product_id, 'Unknown')} to quantity {quantity}.")
        except ValueError:
            print("Invalid input. Use format: product_id,quantity")

    def _handle_remove(self):
        try:
            product_id = int(input("Enter product_id to remove: "))
            self.cart.remove_item(product_id)
            print(f"Removed {self.products.get(product_id, 'Unknown')} from cart.")
        except ValueError:
            print("Invalid input. Enter a valid product_id.")

    def _handle_save_for_later(self):
        try:
            product_id, quantity = map(int, input("Enter product_id,quantity to save for later (e.g., 1,12): ").split(','))
            if self.cart.save_for_later(product_id, quantity, self.products):
                print(f"Saved {quantity} of {self.products.get(product_id, 'Unknown')} for later.")
        except ValueError:
            print("Invalid input. Use format: product_id,quantity")

    def _handle_move_to_cart(self):
        try:
            product_id, quantity = map(int, input("Enter product_id,quantity to move to cart (e.g., 1,12): ").split(','))
            if self.cart.move_to_cart(product_id, quantity, self.products):
                print(f"Moved {quantity} of {self.products.get(product_id, 'Unknown')} to cart.")
        except ValueError:
            print("Invalid input. Use format: product_id,quantity")


if __name__ == "__main__":
    app = GroceryApp()
    app.start()
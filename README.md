GroceryApp – Project Report

📁 Project Structure
| File Name           | Description                                    |
| ------------------- | ---------------------------------------------- |
| `grocery_app.py`    | Main terminal-based Python application         |
| `products.json`     | Contains product IDs and names                 |
| `pricing.json`      | Contains product IDs and respective prices     |
| `transactions.json` | Stores transaction history after each checkout |
| `feedback.json`     | Stores customer feedback with timestamps       |


🎯 Purpose
This project simulates a terminal-based Grocery Point of Sale (POS) system that allows customers to:

  View available grocery products
  Add, update, or remove items from their cart
  Save items for later
  Move saved items back to the cart
  Proceed to checkout and view invoice
  Provide feedback after the purchase
All customer interactions and data are stored using JSON files for easy access and structured storage.

👥 Role Simulated
🧑 Customer:
  Views product list and pricing
  Adds items to cart
  Updates or removes items from cart
  Saves items for later
  Moves saved items back to cart
  Checks out and gets a printable invoice
  Gives optional feedback

🔁 Functional Flow
1.Startup: The app initializes all required JSON files if they don't exist.

2.Product Display: Reads and displays products from products.json and prices from pricing.json.

3.Cart Actions: Customers can:

  Add items to cart
  
  Update quantity or remove items
  
  Save items for later or move them back to cart

4.Checkout:

  Cart total is calculated using pricing.json
  
  Unique transaction ID is generated using uuid
  
  Transaction is saved in transactions.json
  
  Invoice is displayed with date & time

5.Feedback:

  Customer is asked for optional feedback
  
  Stored in feedback.json


🔧 Concepts Practiced
| Concept                | Description                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| **JSON Handling**      | Used to read/write structured data like products, prices, and feedback |
| **Dictionaries**       | Used for storing cart items, saved items, and lookup data              |
| **Classes**            | Implemented using Object-Oriented Programming (OOP) principles         |
| **UUID**               | Ensures each transaction has a unique identifier                       |
| **Datetime**           | Adds timestamp to invoices and feedback                                |
| **Input Validation**   | Ensures valid user inputs for product ID and quantity                  |
| **Loops & Conditions** | Manages program flow, user prompts, and actions                        |


⚠️ Edge Cases Handled
| Edge Case                  | Handling Strategy                                            |
| -------------------------- | ------------------------------------------------------------ |
| Invalid product ID         | Error message shown; input is rejected                       |
| Quantity ≤ 0               | Automatically removes the product from the cart              |
| Non-existent product input | Inform the user and do not proceed with the action           |
| Cart is empty              | Prevents invoice generation                                  |
| Skipped feedback           | Stored as `"No feedback provided"`                           |
| Missing JSON files         | Created automatically using `initialize_json_files()` method |


🗂️ Why JSON Instead of CSV?
| Feature                   | JSON                              | CSV                   |
| ------------------------- | --------------------------------- | --------------------- |
| Supports Nested Data      | ✅ Yes                             | ❌ No                  |
| Object-Oriented Mapping   | ✅ Easy with Python dicts          | ❌ Requires conversion |
| Readability for Hierarchy | ✅ Clear structure                 | ❌ Flat rows only      |
| Transaction Structure     | ✅ Can store dicts, lists together | ❌ Only flat columns   |
| Timestamp & Metadata      | ✅ Easily supported                | ✅ But less organized  |


✅ Conclusion:
JSON is a better fit for this project because:
  It allows nested objects like {product_id: quantity} in transactions.
  It aligns naturally with Python’s dict and list types.
  It’s easy to manage structured data (e.g., transactions, invoices, feedback) with minimal transformation.

✅ Summary of Core Classes and Responsibilities
| Class              | Responsibility                                                 |
| ------------------ | -------------------------------------------------------------- |
| `JSONHandler`      | Initializes and manages reading/writing of JSON files          |
| `Cart`             | Manages cart and saved-for-later item operations               |
| `InvoiceGenerator` | Generates and prints customer invoice with total and timestamp |
| `PaymentProcessor` | Calculates total amount from cart items using price lookup     |
| `FeedbackManager`  | Collects and stores user feedback                              |
| `GroceryApp`       | Main workflow: manages interaction, cart actions, and checkout |

📌 Final Thoughts
This SmartGroceryApp is a well-organized, single-role terminal-based POS system. It demonstrates practical skills in:
  File handling with JSON
  Clean object-oriented programming
  User input handling and validation
  Data persistence
  Invoice generation with real-time logic


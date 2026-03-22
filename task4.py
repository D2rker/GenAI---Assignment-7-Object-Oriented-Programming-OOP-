# --- STEP 1: The Parent Class (Must be first!) ---
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # Private attribute (Encapsulation)
        self.category = category

    def get_price(self):
        return self.__price

    def get_info(self):
        print(f"Product: {self.name} | Price: ${self.__price}")

# --- STEP 2: The Subclasses (Inheritance) ---
class Laptop(Product):
    def get_info(self):
        # Specific style for Laptops (Method Overriding)
        print(f"[LAPTOP] Model: {self.name} | Price: ${self.get_price()}")

class Mobile(Product):
    def get_info(self):
        # Specific style for Mobiles (Method Overriding)
        print(f"[MOBILE] Device: {self.name} | Category: {self.category} | Price: ${self.get_price()}")

# --- STEP 3: The Polymorphism Loop ---
# We store different types of objects in one list
inventory = [
    Laptop("MacBook Pro", 2400, "Electronics"),
    Mobile("iPhone 15", 999, "Electronics"),
    Laptop("Dell XPS", 1500, "Electronics")
]

print("--- Inventory Report ---")
for item in inventory:
    # This is Polymorphism:
    # One method call ('get_info') behaves differently depending on the object!
    item.get_info()
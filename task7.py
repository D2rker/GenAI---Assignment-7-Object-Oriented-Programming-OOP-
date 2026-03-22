# --- Base Class (from Task 6) ---
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Product({self.name}, ${self.__price}, {self.category})"

    def __add__(self, other):
        return self.__price + other.get_price()


# --- Task 7: Inventory Class ---
class Inventory:
    def __init__(self):
        self.products = []  # List to store product objects

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        # We filter the list to keep everything EXCEPT the product with that name
        self.products = [p for p in self.products if p.name != name]

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.get_price()
        return total

    def show_all_products(self):
        for p in self.products:
            print(p)


# --- Task 7: Store Class (Composition) ---
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()  # Store "has an" Inventory

    def add_new_product(self):
        print(f"\n--- Adding new product to {self.store_name} ---")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")

        new_prod = Product(name, price, category)
        self.inventory.add_product(new_prod)
        print(f"Success: {name} added.")

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Inventory Value: ${self.inventory.get_total_value()}")


# --- TESTING THE SYSTEM ---

# 1. Creating a Store object
my_store = Store("Tech Haven")

# 2. Adding 3 products (using the input method)
for i in range(3):
    my_store.add_new_product()

# 3. Showing summary
my_store.show_summary()

# 4. Using __add__ to combine prices of two products
# Let's take the first two products added to the inventory
if len(my_store.inventory.products) >= 2:
    p1 = my_store.inventory.products[0]
    p2 = my_store.inventory.products[1]
    combined_price = p1 + p2
    print(f"\n[Operator Overloading] Price of {p1.name} + {p2.name} = ${combined_price}")
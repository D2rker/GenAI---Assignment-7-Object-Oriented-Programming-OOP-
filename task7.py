# task 7- Mini project: simple inventry system

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price 
        self.category = category

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.__price}"

    def __add__(self, other):
        return self.__price + other.get_price()

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.get_price()
        return total

    def show_all_products(self):
        if not self.products:
            print("Inventory is empty.")
        for p in self.products:
            print(p)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory() 

    def show_summary(self):
        self.inventory.show_all_products()
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Value: ${self.inventory.get_total_value()}")
        print("-" * 35)

my_store = TechStore = Store("Gamer Gear Hub")

product1 = Product("Mechanical Keyboard", 120.0, "Peripherals")
product2 = Product("Gaming Mouse", 80.0, "Peripherals")
product3 = Product("UltraWide Monitor", 450.0, "Displays")

my_store.inventory.add_product(product1)
my_store.inventory.add_product(product2)
my_store.inventory.add_product(product3)

my_store.show_summary()

combined = product1 + product2
print(f"Combined price of {product1.name} and {product2.name} is ${combined}")

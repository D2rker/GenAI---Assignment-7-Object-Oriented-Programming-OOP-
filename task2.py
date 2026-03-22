class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # Private attribute
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than 0.")

    def get_info(self):
        print(f"Product: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.__price}")
        print("-" * 20)


product = Product("Smartphone", 800, "Electronics")

print(f"Initial Price: ${product.get_price()}")

# Testing a valid price update
product.set_price(750)
print(f"Updated Price: ${product.get_price()}")

# Testing an invalid price update
product.set_price(-50)
print(f"Price after invalid attempt: ${product.get_price()}")
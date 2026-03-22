class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    # 1. The __str__ method: Defines what happens when you print(object)
    def __str__(self):
        return f"Product({self.name}, {self.__price}, {self.category})"

    # 2. The __add__ method: Defines behavior for the + operator
    def __add__(self, other):
        # We add the prices of 'self' (the left object) and 'other' (the right object)
        return self.__price + other.get_price()

# --- Testing Magic Methods ---

p1 = Product("Keyboard", 50, "Accessories")
p2 = Product("Mouse", 30, "Accessories")

# Testing __str__
# Instead of seeing <__main__.Product object at 0x...>, we see our readable string:
print(f"Product 1: {p1}")
print(f"Product 2: {p2}")

# Testing Operator Overloading (__add__)
total_cart_value = p1 + p2
print(f"Total Combined Price: ${total_cart_value}")
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price}")
        print("-" * 20)

    # Optional: Method to calculate a discounted price
    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        return self.price - discount_amount


#  first object
product1 = Product("Laptop", 1200, "Electronics")
#  second object
product2 = Product("Coffee Mug", 15, "Kitchenware")

product1.get_info()
product2.get_info()

discounted_price = product1.apply_discount(10)
print(f"Discounted price for {product1.name}: ${discounted_price}")
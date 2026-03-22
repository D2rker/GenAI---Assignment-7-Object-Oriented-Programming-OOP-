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

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        print(f"Product: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.get_price()}")  # Accessing private price via getter
        print(f"Warranty: {self.warranty_years} years")
        print("-" * 20)

laptop = ElectronicProduct("Gaming Laptop", 1500, "Electronics", 2)
laptop.get_info()
from abc import ABC, abstractmethod

# 1. Create the Abstract Base Class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        # This method has no implementation here
        pass

# 2. Subclass for Credit Card
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}...")
        print("Verifying card details... Payment Successful!")

# 3. Subclass for UPI
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}...")
        print("Waiting for PIN entry... Payment Successful!")

# --- Testing the Classes ---

# payment_base = Payment() # This would throw an error if uncommented!

cc_pay = CreditCardPayment()
upi_pay = UPIPayment()

cc_pay.process_payment(1200)
print("-" * 30)
upi_pay.process_payment(450)
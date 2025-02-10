# Importing the ABC module to create abstract base classes
from abc import ABC, abstractmethod

# Define an interface (abstract base class) called PaymentStrategy
# This class will declare a method called process_payment that must be overridden by any subclass
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Implement a concrete class for Credit Card payment that inherits from PaymentStrategy
# This class will provide an implementation for the process_payment method
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} units.")

# Implement a concrete class for PayPal payment that inherits from PaymentStrategy
# This class will provide an implementation for the process_payment method
class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} units.")

# Implement a concrete class for Cryptocurrency payment that inherits from PaymentStrategy
# This class will provide an implementation for the process_payment method
class CryptoPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of {amount} units.")

# Define a context class called PaymentContext that will use a PaymentStrategy object
class PaymentContext:
    
    # Constructor that initializes the strategy with a PaymentStrategy object
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
        
    # Method to change the strategy dynamically
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
        
    # Method to execute the payment using the current strategy
    def execute_payment(self, amount):
        self._strategy.process_payment(amount)

# Example usage of the strategy pattern
if __name__ == "__main__":
    amount = 100  # Define the amount to be processed
    
    # Create a PaymentContext with CreditCardPayment strategy
    context = PaymentContext(CreditCardPayment())
    context.execute_payment(amount)  # Output: Processing credit card payment of 100 units.
    
    # Change the strategy to PayPalPayment and process the payment
    context.set_strategy(PayPalPayment())
    context.execute_payment(amount)  # Output: Processing PayPal payment of 100 units.
    
    # Change the strategy to CryptoPayment and process the payment
    context.set_strategy(CryptoPayment())
    context.execute_payment(amount)  # Output: Processing cryptocurrency payment of 100 units.

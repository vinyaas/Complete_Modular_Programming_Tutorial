from abc import ABC, abstractmethod

# Define the PaymentTemplate abstract base class
class PaymentTemplate(ABC):
    
    # Template method that defines the steps to process a payment
    def process_payment(self, amount):
        self.authenticate()  # Step 1: Authenticate the user
        self.initialize_transaction()  # Step 2: Initialize the transaction
        self.deduct_amount(amount)  # Step 3: Deduct the amount (abstract method to be implemented by subclasses)
        self.confirm_transaction()  # Step 4: Confirm the transaction
        
    def authenticate(self):
        print('Authenticating the user')  # Print a message indicating user authentication
        
    def initialize_transaction(self):
        print('Initializing the transaction')  # Print a message indicating transaction initialization
        
    @abstractmethod
    def deduct_amount(self, amount):
        pass  # Abstract method for deducting the amount, to be implemented by subclasses
    
    def confirm_transaction(self):
        print('Confirming transaction')  # Print a message indicating transaction confirmation

# Concrete class for Credit Card payment
class CreditCardPayment(PaymentTemplate):
    def deduct_amount(self, amount):
        print(f"Deducting {amount} units from credit card")  # Specific implementation for deducting amount from credit card

# Concrete class for PayPal payment
class PayPalPayment(PaymentTemplate):
    def deduct_amount(self, amount):
        print(f"Deducting {amount} units from PayPal account")  # Specific implementation for deducting amount from PayPal account

# Main block to execute the payment processing
if __name__ == "__main__":
    amount = 100  # Amount to be processed

    # Using Credit Card Payment
    print("Processing Credit Card Payment:")
    credit_card_payment = CreditCardPayment()  # Create an instance of CreditCardPayment
    credit_card_payment.process_payment(amount)  # Process the payment using credit card

    # Using PayPal Payment
    print("\nProcessing PayPal Payment:")
    paypal_payment = PayPalPayment()  # Create an instance of PayPalPayment
    paypal_payment.process_payment(amount)  # Process the payment using PayPal

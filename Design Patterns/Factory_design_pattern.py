from abc import ABC , abstractmethod

# Define the product class

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self , amount):
        pass
    
# Define concrete class for each payment method 

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} units.")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} units.")

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of {amount} units.")

# Implementing the Factory 

class PaymentFactory:
    @staticmethod
    def create_payment_method(method_type):
        if method_type == 'credit_card':
            return CreditCardPayment()
        elif method_type == 'paypal':
            return PayPalPayment()
        elif method_type == 'bank_transfer':
            return BankTransferPayment()
        else:
            raise ValueError(f"Unknown payment method type: {method_type}")

# Keeping this seperate because of exception handling which isnt part of code logic 
def process_customer_payment(method_type , amount):
    try :
        payment_method = PaymentFactory.create_payment_method(method_type)
        payment_method.process_payment(amount)
    except ValueError as e:
        print(f'Failed to process payment')
        
if __name__ == "__main__":
    process_customer_payment('credit_card', 100)
    process_customer_payment('paypal', 150)
    process_customer_payment('bank_transfer', 200)
    process_customer_payment('crypto', 250)  # This will raise an error and be handled

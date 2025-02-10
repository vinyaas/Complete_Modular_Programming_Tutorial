# Introduction to Abstraction
# Abstraction is a fundamental concept in programming that allows us to hide the implementation details of an object or system and only show the necessary information to the outside world.
# It helps to reduce complexity, improve modularity, and increase reusability of code.

# In modular programming, abstraction is used to create independent modules that can be easily combined to form a larger system.
# Each module can be designed, implemented, and tested independently without affecting the other modules.

# In Python, abstraction can be achieved using classes and objects.
# A class defines the structure and behavior of an object, while an object is an instance of a class.

# Example of Abstraction in Python
class BankAccount:
    # The class BankAccount abstracts the details of a bank account
    def __init__(self, account_number, balance):
        # The account number and balance are private attributes, which means they can't be accessed directly from outside the class
        self.__account_number = account_number
        self.__balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        # The deposit method modifies the private balance attribute
        self.__balance += amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # The withdraw method checks if the withdrawal amount is greater than the balance and modifies the private balance attribute
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    # Method to get the account balance
    def get_balance(self):
        # The get_balance method returns the private balance attribute
        return self.__balance

# Create an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Deposit money into the account
account.deposit(500)

# Withdraw money from the account
account.withdraw(200)

# Get the account balance
print("Account balance:", account.get_balance())

# Key Concepts of Abstraction
# 1. **Encapsulation**: The idea of bundling data and methods that operate on that data within a single unit, such as a class or object.
# 2. **Abstraction**: The idea of hiding the implementation details of an object or system and only showing the necessary information to the outside world.
# 3. **Modularity**: The idea of breaking down a large system into smaller, independent modules that can be easily combined to form a larger system.
# 4. **Interface**: The set of methods and attributes that an object or module exposes to the outside world.

# Benefits of Abstraction
# 1. **Reduced complexity**: Abstraction helps to reduce the complexity of a system by hiding the implementation details and only showing the necessary information.
# 2. **Improved modularity**: Abstraction helps to improve modularity by allowing us to design, implement, and test independent modules without affecting the other modules.
# 3. **Increased reusability**: Abstraction helps to increase reusability of code by allowing us to use the same module or class in different contexts.

# Common Use Cases of Abstraction in Data Science Projects
# 1. **Data preprocessing**: Abstraction can be used to create a module that preprocesses data, such as handling missing values, encoding categorical variables, and scaling numerical variables.
# 2. **Model training**: Abstraction can be used to create a module that trains a machine learning model, such as a neural network or decision tree.
# 3. **Model evaluation**: Abstraction can be used to create a module that evaluates the performance of a machine learning model, such as calculating accuracy, precision, and recall.



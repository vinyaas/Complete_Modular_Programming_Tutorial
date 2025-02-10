# Abstract Methods
# Abstract methods are methods that are declared in a class but not implemented.
# They are used to define a method that must be implemented by any subclass of the class.
# Abstract methods are typically used in abstract classes, which are classes that cannot be instantiated and are intended to be inherited by other classes.

from abc import ABC , abstractmethod

class PaymentGateway(ABC):
    
    @abstractmethod
    def process_payment(self , amount):
        pass
    
class CreditCard(PaymentGateway):
    
    def __init__(self , card_number , expiration_date , cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date 
        self.cvv = cvv 
        
    def process_payment(self, amount):
        print('Processing payment of $' , amount , "using credit card" , self.card_number)
        return True
    
class PayPal(PaymentGateway):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def process_payment(self, amount):
        print("Processing payment of $", amount, "using PayPal account", self.email)
        return True
    
credit_card = CreditCard("1234-5678-9012-3456", "12/2025", "123")
print("Credit card payment:", credit_card.process_payment(100))

paypal = PayPal("example@example.com", "password123")
print("PayPal payment:", paypal.process_payment(100))

# Why Abstract Methods are Used
# 1. **To define an interface**: Abstract methods are used to define an interface that must be implemented by any subclass of the class.
# 2. **To provide a common base class**: Abstract methods are used to provide a common base class for related classes.
# 3. **To enforce implementation**: Abstract methods are used to enforce implementation of a method by subclasses.

# Where Abstract Methods are Used
# 1. **In abstract classes**: Abstract methods are used in abstract classes to define methods that must be implemented by subclasses.
# 2. **In interfaces**: Abstract methods are used in interfaces to define methods that must be implemented by classes that implement the interface.
# 3. **In modular programming**: Abstract methods are used in modular programming to define methods that can be implemented by different modules.

# Contribution of Abstract Methods in Modular Programming
# 1. **Modularity**: Abstract methods contribute to modularity by allowing different modules to implement the same method in different ways.
# 2. **Reusability**: Abstract methods contribute to reusability by allowing the same method to be used in different contexts.
# 3. **Flexibility**: Abstract methods contribute to flexibility by allowing different modules to implement the same method in different ways.

# Contribution of Abstract Methods in Data Science End-to-End Projects
# 1. **Data preprocessing**: Abstract methods can be used to define methods for data preprocessing, such as handling missing values and encoding categorical variables.
# 2. **Model training**: Abstract methods can be used to define methods for model training, such as training a neural network or a decision tree.
# 3. **Model evaluation**: Abstract methods can be used to define methods for model evaluation, such as calculating accuracy or precision.

# Example of Abstract Methods in Data Science

import pandas as pd
from abc import abstractmethod , ABC
class DataPreprocessor(ABC):
    # The DataPreprocessor class is an abstract class that defines an abstract method called preprocess.
    @abstractmethod
    def preprocess(self, data):
        # The preprocess method is not implemented in the DataPreprocessor class, but it must be implemented by any subclass of DataPreprocessor.
        pass

class NumericalDataPreprocessor(DataPreprocessor):
    # The NumericalDataPreprocessor class is a subclass of DataPreprocessor that implements the preprocess method.
    def preprocess(self, data):
        # The preprocess method is implemented in the NumericalDataPreprocessor class to preprocess numerical data.
        return data.fillna(data.mean())

class CategoricalDataPreprocessor(DataPreprocessor):
    # The CategoricalDataPreprocessor class is a subclass of DataPreprocessor that implements the preprocess method.
    def preprocess(self, data):
        # The preprocess method is implemented in the CategoricalDataPreprocessor class to preprocess categorical data.
        return pd.get_dummies(data, columns=['category'])

# Create an object of the NumericalDataPreprocessor class
numerical_preprocessor = NumericalDataPreprocessor()
data = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': [4, 5, 6]
})
print("Preprocessed data:", numerical_preprocessor.preprocess(data))

# Create an object of the CategoricalDataPreprocessor class
categorical_preprocessor = CategoricalDataPreprocessor()
data = pd.DataFrame({
    'category': ['A', 'B', 'A']
})
print("Preprocessed data:", categorical_preprocessor.preprocess(data))

# In this example, the DataPreprocessor class defines an abstract method called preprocess that must be implemented by any subclass of DataPreprocessor.
# The NumericalDataPreprocessor and CategoricalDataPreprocessor classes are subclasses of DataPreprocessor that implement the preprocess method.
# The preprocess method is used to preprocess numerical and categorical data.

# Best Practices for Using Abstract Methods in Data Science
# 1. **Use abstract methods to define interfaces**: Use abstract methods to define interfaces that must be implemented by subclasses.
# 2. **Use abstract methods to provide a common base class**: Use abstract methods to provide a common base class for related classes.
# 3. **Use abstract methods to enforce implementation**: Use abstract methods to enforce implementation of a method by subclasses.

# Common Use Cases for Abstract Methods in Data Science
# 1. **Data preprocessing**: Abstract methods can be used to define methods for data preprocessing, such as handling missing values and encoding categorical variables.
# 2. **Model training**: Abstract methods can be used to define methods for model training, such as training a neural network or a decision tree.
# 3. **Model evaluation**: Abstract methods can be used to define methods for model evaluation, such as calculating
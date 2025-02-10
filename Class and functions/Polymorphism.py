class MathOperation:
    """
    Base class for mathematical operations.
    """
    def execute(self, a, b):
        """
        Method to perform the operation. 
        Should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def execute(self, a, b, c):
        """
        Overloaded method to perform the operation with three inputs.
        This will show how method overloading is typically managed in Python (note: Python does not support method overloading natively).
        """
        raise NotImplementedError("Subclasses should implement this method")

class Addition(MathOperation):
    def execute(self, a, b):
        """
        Method overriding example: Perform addition of two numbers.
        """
        return a + b

    def execute(self, a, b, c):
        """
        Overloaded method to perform addition of three numbers.
        """
        return a + b + c

class Subtraction(MathOperation):
    def execute(self, a, b):
        """
        Method overriding example: Perform subtraction of two numbers.
        """
        return a - b

    def execute(self, a, b, c):
        """
        Overloaded method to perform subtraction of three numbers.
        """
        return a - b - c

# Example usage
def perform_operation(operation, *args):
    if len(args) == 2:
        return operation.execute(args[0], args[1])
    elif len(args) == 3:
        return operation.execute(args[0], args[1], args[2])
    else:
        raise ValueError("Unsupported number of arguments")

# Creating objects for each operation
addition = Addition()
subtraction = Subtraction()

# Performing operations
print(f"Addition of 2 and 3: {perform_operation(addition, 2, 3)}")
print(f"Addition of 2, 3, and 4: {perform_operation(addition, 2, 3, 4)}")
print(f"Subtraction of 5 and 3: {perform_operation(subtraction, 5, 3)}")
print(f"Subtraction of 5, 3, and 1: {perform_operation(subtraction, 5, 3, 1)}")

# Polymorphism in Data Science
# Definition: Polymorphism is a concept where objects of different classes can be treated as objects of a common base class. 
# This allows for methods to be used interchangeably without needing to know the exact class of the object.

# Advantages in Data Science:

# Flexibility: You can use different types of models or operations interchangeably, making the code more adaptable to changes.
# Maintainability: Easier to maintain and extend code. Adding new operations or models doesn’t require changes to the existing code.
# Abstraction: Allows for working at a higher level of abstraction, focusing on what operations need to be performed rather than how they are performed.
# Reusability: Promotes code reuse by implementing common interfaces that can be used across different models or operations.

# When and Where to Use:

# Model Training and Evaluation: When implementing different machine learning models, you can create a common interface for training and evaluation.
# Data Processing Pipelines: For preprocessing steps where different types of preprocessing may be applied to the same dataset.
# Utility Functions: For functions that need to handle various types of input data or objects.

# Example: In a scenario where you have different models like LinearRegression and DecisionTreeRegressor, you can create a common interface for training and evaluating these models.

# Method Overloading
# Definition: Method overloading is the ability to create multiple methods with the same name but different parameters.
# However, Python does not support method overloading natively; it can be simulated using default arguments or variable-length arguments.

# Advantages:

# Code Clarity: Improves readability by using the same method name for similar operations with different parameters.
# Functionality Flexibility: Allows defining different behaviors for the same method based on different inputs.
# When and Where to Use:
# Data Processing: Methods to preprocess data differently based on the number or type of input parameters.
# Utility Functions: Functions that need to handle various types of inputs for similar operations.


# Method Overriding
# Definition: Method overriding occurs when a derived class provides a specific implementation of a method that is already defined in its base class.
# This allows the derived class to alter or extend the functionality of the base class method.

# Advantages:

# Customization: Allows for customizing or extending the behavior of inherited methods.
# Polymorphism: Enables polymorphic behavior where the derived class method is called, even when using a reference to the base class.

# When and Where to Use:
# Model Training: When different models require specific training implementations.
# Data Processing: When different types of data need specific preprocessing methods.
# Custom Operations: When subclasses need to provide specific implementations of operations defined in a base class.


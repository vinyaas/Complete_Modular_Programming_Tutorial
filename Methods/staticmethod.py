class calculator: 
    
    @staticmethod
    def add(x , y):
        return x + y 
    
    def multiply(x,y):
        return x * y
    
c = calculator
print(c.add(3,3,))
print(c.multiply(3,6))
    
# Explanation of the Benefits of Using @staticmethod

# Clarity of Intent:
# Using the @staticmethod decorator makes it explicit that the method does not modify or depend on the class or instance state.
# It signals to other developers that this is a utility method related to the class but does not interact with class or instance variables.

# Namespace Grouping:
# Static methods are grouped within the class namespace, which logically organizes related functions and makes the codebase easier to navigate and maintain.

# Documentation and Code Organization:
# It helps in documenting the code better. When reading the class, it's clear which methods are static and which are instance-specific.

# Avoiding Unintended Behavior:
# If you accidentally call an instance method without the self parameter, you can end up with bugs. Using @staticmethod ensures that the method is treated as a standalone function.

# Example of not using @staticmethod:
# class Calculator:
#     def add(x, y):
#         return x + y
# c = Calculator
# print(c.add(3, 3))  # Output: 6

# Example of using @staticmethod for better clarity and intent:
# class Calculator:
#     @staticmethod
#     def add(x, y):
#         return x + y
# c = Calculator
# print(c.add(3, 3))  # Output: 6

# In both examples, c.add(3, 3) works, but using @staticmethod makes the code self-explanatory and avoids potential misuse.

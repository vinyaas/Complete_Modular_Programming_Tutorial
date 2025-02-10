# Define the decorator function
def my_decorator(func):
    # Define the wrapper function
    def wrapper():
        # Print a message before calling the original function
        print("Something is happening before the function is called.")
        # Call the original function
        func()
        # Print a message after calling the original function
        print("Something is happening after the function is called.")
    # Return the wrapper function
    return wrapper

# Apply the decorator to the say_hello function.
@my_decorator
def say_hello():
    # Print a greeting message
    print("Hello!")
    
# @my_decorator: This syntax applies the my_decorator to the say_hello function. 
# It is equivalent to say_hello = my_decorator(say_hello).

# Call the decorated say_hello function
say_hello()
#-------------------------------------------------------------------------------------------------------------#

# Decorators are primarily used to add functionality such as logging, caching, validation,
# and other repetitive tasks to functions or methods. While they aren't typically used
# to change the core logic of a function, they can be incredibly useful for enhancing and
# managing cross-cutting concerns in a clean and modular way.

# Common Use Cases for Decorators:

# Logging:
# Track the execution of functions, log function calls, and record outputs.

# Caching (Memoization):
# Store the results of expensive function calls and reuse them to improve performance.

# Validation:
# Check the validity of inputs before executing the main function logic.

# Authentication:
# Ensure that a user is authenticated before allowing access to certain functions.

# Performance Monitoring:
# Measure the execution time of functions to identify and optimize performance bottlenecks.

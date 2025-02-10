# Define the logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Define the timing decorator
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

# Define the validation decorator
def validate_decorator(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args[0]):
            raise ValueError("All elements in the data list must be numbers")
        return func(*args, **kwargs)
    return wrapper

# Define the data processing function with multiple decorators
@log_decorator
@timing_decorator
@validate_decorator
def process_data(data):
    return sum(data)

# Use the decorated function
data = [1, 2, 3, 4, 5]
result = process_data(data)
print(f"Processed data result: {result}")

# What Happens Here:
# Decorator Definition: log_decorator is defined to take a function func and wrap it with additional logging logic.
# Applying the Decorator: The @log_decorator syntax applies the decorator to the add function, replacing it with the wrapper function.
# Function Execution: When add(3, 5) is called, it actually executes wrapper(3, 5),
# which logs the call, runs the original add function, logs the result, and returns it.


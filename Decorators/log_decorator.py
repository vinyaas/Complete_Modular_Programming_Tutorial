def log_decorator(func):
    def wrapper(self, *args):
        print(f"Calling {func.__name__} with arguments {args} ")
        result = func(self, *args)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

class Calculator:
    
    @log_decorator
    def add(self, x, y):
        return x + y
    
    @log_decorator
    def subtract(self, x, y):
        return x - y
    
    @log_decorator
    def multiply(self, x, y):
        return x * y
    
    @log_decorator
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
calc = Calculator()

print(calc.add(3, 4))
print(calc.subtract(10, 5))



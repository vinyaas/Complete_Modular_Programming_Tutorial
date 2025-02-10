class Calculator:
    # Class variable to keep track of the total number of operations
    total_operations = 0
    
    def add(self, x, y):
        # Instance method to perform addition
        # Increment the class variable total_operations by 1
        Calculator.total_operations += 1
        return x + y
    
    def multiply(self, x, y):
        # Instance method to perform multiplication
        # Increment the class variable total_operations by 1
        Calculator.total_operations += 1
        return x * y
    
    def divide(self, x, y):
        # Instance method to perform division
        # Increment the class variable total_operations by 1
        Calculator.total_operations += 1
        if y != 0:
            return x / y
        else:
            raise ValueError('Cannot divide by zero')
        
    @classmethod
    def get_total_operations(cls):
        # Class method to access the total number of operations
        # Return the class variable total_operations
        return cls.total_operations

# Create an instance of the Calculator class
calc1 = Calculator()
# Create another instance of the Calculator class
calc2 = Calculator()

# Perform addition using calc1 instance
print(calc1.add(3, 2))  # Output: 5
# Perform addition using calc2 instance
print(calc2.add(4, 5))  # Output: 9

# Perform multiplication using calc1 instance
print(calc1.multiply(3, 8))  # Output: 24
# Perform division using calc2 instance
print(calc2.divide(3, 6))    # Output: 0.5

# Access the total number of operations using the class method
print(calc1.get_total_operations())  # Output: 4

#-------------------------------------------------------------------------#
class Person:
    
    def __init__(self , name , age):
        self.age = age
        self.name = name
        
    @classmethod
    def from_birth_year(cls ,name, birthyear):
        age = 2024 - birthyear
        return cls(name , age)
    
person = Person.from_birth_year('alice' , 1990)
print(person.name , person.age)

# this method allows u to access single properties such as name of person or jus age .

#----------------------------------------------------------------------------------------------#

class Student:
    
    def __init__(self , name , age):
        self.age = age
        self.name = name
        
    @classmethod
    def from_birthyear(cls , name , birthyear):
        age = 2024 - birthyear
        return cls(name , age)
    
student = Student.from_birthyear('vinyas' , 1976)
print(student.name)
print(student.age)

#-------------------------------------------------------------# 
class Employee:
    
    employee_count = 0
    
    def add_emp(self):
        Employee.employee_count += 4
        
    @classmethod
    def count(cls):
        return cls.employee_count
    
new = Employee()
new.add_emp()
print(new.count())
        

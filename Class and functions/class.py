class Person:
    
    #instance attributes 
    def __init__(self,name,age,gender):
        self.age = age
        self.name = name
        self.gender = gender
    
    #instance method
    def introduce(self):
        return f"My name is {self.name} and my age is {self.age} and am a {self.gender}"

#instantiate the person class 
if __name__ == '__main__':
    
    person1 = Person('alice' , 23 , 'female')
    person2 = Person('george' , 45 , 'male')

    print(person1.introduce())
    print(person2.introduce())

# Explanation of the Example

# Class Definition:
# We define a Person class with an __init__ method to initialize the attributes name, age, and gender.

# Initialization of State:
# The __init__ method initializes these attributes when a new Person object is created. 
# This ensures that every Person object has a unique set of values for name, age, and gender.

# Object Identity:
# The attributes name, age, and gender define the identity of each Person object.
# They hold values specific to each instance and are essential for describing the person.

# Persistent State:
# The attributes initialized in __init__ are stored as instance variables (self.name, self.age, self.gender).
# These variables persist throughout the object's lifecycle and can be used by other methods in the class.

# Instance-Specific Behavior:
# The introduce method uses the instance-specific attributes to provide a personalized introduction.
# Each Person object will have a different introduction based on its initialized attributes.


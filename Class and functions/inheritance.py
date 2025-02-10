# Inheritance in Python

# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (child class)
# to inherit attributes and methods from another class (parent class). This facilitates code reuse, 
# logical hierarchy, and the implementation of shared functionality across different classes.

# Key Concepts of Inheritance:
# 1. Parent Class (Superclass): The class whose properties and methods are inherited.
# 2. Child Class (Subclass): The class that inherits from the parent class.
# 3. Method Overriding: The child class can override methods of the parent class to provide specific implementations.
# 4. Super(): A function used to call methods from the parent class in the child class.

# Using Inheritance in Data Science Projects

# Inheritance is particularly useful in data science projects for structuring the code, improving maintainability, 
# and promoting reusability across various stages of the data science workflow. Here’s how inheritance can be applied 
# in an end-to-end data science project:

# 1. Data Preprocessing
# - Parent Class: A general DataPreprocessor class can be created with common methods for data cleaning, normalization, encoding, etc.
# - Child Classes: Specialized preprocessors for different types of data (e.g., TextDataPreprocessor, ImageDataPreprocessor) can inherit
#   from DataPreprocessor and implement specific preprocessing steps required for text, images, or other data types.

# 2. Feature Engineering
# - Parent Class: A FeatureEngineer class might include basic methods for feature selection, scaling, and transformation.
# - Child Classes: Specific feature engineering techniques for different domains (e.g., TimeSeriesFeatureEngineer, NLPFeatureEngineer) 
#   can extend the parent class to add domain-specific feature engineering methods.

# 3. Model Building and Training
# - Parent Class: A generic Model class can define methods for model initialization, training, and evaluation.
# - Child Classes: Specific models like LinearRegressionModel, RandomForestModel, or NeuralNetworkModel can inherit from the 
#   Model class and provide implementations tailored to their respective algorithms.

# 4. Pipeline Management
# - Parent Class: A Pipeline class can manage the workflow of data preprocessing, feature engineering, model training, and evaluation.
# - Child Classes: Pipelines for different tasks or types of data (e.g., TextClassificationPipeline, ImageClassificationPipeline)
#   can inherit from the Pipeline class and customize the workflow steps as needed.

# 5. Custom Metrics and Evaluation
# - Parent Class: An Evaluator class can be created to define common evaluation metrics and methods.
# - Child Classes: Specific evaluation methods for different types of models or tasks (e.g., ClassificationEvaluator, RegressionEvaluator)
#   can extend the parent class to include additional metrics and methods relevant to the task.

# 6. Deployment and Integration
# - Parent Class: A Deployer class can include methods for deploying models to various platforms (e.g., cloud services, local servers).
# - Child Classes: Specific deployment strategies (e.g., AWSDeployer, AzureDeployer) can inherit from the Deployer class and 
#   provide implementations for deploying models to specific environments.

#----------------------------------------------------------------------------------------------------------------------------------------#

#Parent Class
class Calculator:
    def __init__(self):
        pass  # Constructor for the Calculator class, does nothing for now
    
    def add(self , x, y):
        return x + y  
    
    def subtract(self , x, y):
        if x > y:
            return x - y  
        return y - x  

#Child Class
class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()  
        
    def multiply(self , x , y):
        return x * y 
        
    def divide(self , x , y):
        if y != 0 :
            return x / y  
        raise ValueError('Y value must be greater than zero') 
        
    # Method Overriding 
    def add(self , x , y):
        print(f"Adding {x} and {y} in scientific calculator")  # Print a message before adding
        return super().add(x, y)  # Call the add method from the parent class
        
calc = ScientificCalculator()
print(calc.add(4, 5))  
print(calc.subtract(4, 5)) 
print(calc.multiply(3, 4))  

# Explanation
# Parent Class (Calculator):
# This class provides basic arithmetic operations: add and subtract.

# Child Class (ScientificCalculator):
# This class inherits from Calculator, meaning it can use add and subtract methods.
# It introduces new methods: multiply and divide.
# It overrides the add method to add a print statement before calling the parent class's add method using super().

# Summary
# Parent Class (Calculator): Provides basic arithmetic functions.
# Child Class (ScientificCalculator): Inherits from Calculator, adds new methods, and overrides the add method.
# Method Overriding: The add method in ScientificCalculator overrides the add method in Calculator.
# Using super(): The overridden add method in ScientificCalculator uses super() to call the add method from the parent class.
#------------------------------------------------------------------------------------------------------------------------#

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataPreprocessor:
    
    def __init__(self, data):
        self.data = data
        
    def fill_missing_data(self):
        self.data.fillna(0, inplace=True)
        
    def standardize_data(self, columns):
        scaler = StandardScaler()
        self.data[columns] = scaler.fit_transform(self.data[columns])
        
class HouseDataPreprocessor(DataPreprocessor):
        
    def encode(self):
        self.data['location'] = LabelEncoder().fit_transform(self.data['location'])

# Sample DataFrame
df = pd.DataFrame({
    'size': [1400, 1600, 1700, 1875, 1100], 
    'bedrooms': [3, 3, 3, 4, 2], 
    'location': ['Downtown', 'Uptown', 'Suburb', 'Downtown', 'Suburb'], 
    'price': [300000, 340000, 360000, 380000, 250000]
})

# Instantiate the HouseDataPreprocessor with the DataFrame
processor = HouseDataPreprocessor(df)

# Fill missing data
processor.fill_missing_data()

# Encode categorical 'location' data
processor.encode()

# Standardize the numerical columns
processor.standardize_data(['size', 'bedrooms', 'price'])

# Get the processed DataFrame
df = processor.data
print(df)

#------------------------------------------------------------------------------------------------------------------#


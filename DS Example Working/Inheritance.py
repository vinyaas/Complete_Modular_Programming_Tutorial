
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class DataProcessor:
    """
    Base class for data processing
    """
    
    def __init__(self , data:pd.DataFrame , target_column:str):
        self.data = data 
        self.target_column = target_column
        self.features = data.drop(columns=[target_column])
        self.target = data[target_column]
        self.scaler = StandardScaler()
        
    def process_data(self):
        """
        Preprocess the data by scaling the features
        """
        self.features = self.scaler.fit_transform(self.features)
        
    def split_data(self , test_size: float = 0.2):
        """
        split the data to test and train sets
        """
        self.x_train , self.x_test , self.y_train , self.y_test = train_test_split(self.features , self.target , test_size=test_size , random_state=42)
        
    def standardize_data(self):
        self.x_train = self.scaler.fit_transform(self.x_train)
        self.x_test = self.scaler.transform(self.x_test)
        
    def get_data(self):
        """
        returns the training and test data
        """
        return self.x_train , self.x_test , self.y_train , self.y_test
    
class LinearRegressionModel(DataProcessor):
    """
    Derived class for linear regression model
    """
    def __init__(self, data:pd.DataFrame , target_column :str):
        super().__init__(data , target_column)
        self.model = LinearRegression()
    
    def train_model(self):
        """
        Train the linear regression model
        """
        self.model.fit(self.x_train , self.y_train)
    
    # Method Overriding
    def evaluate_model(self):
        """
        Evaluate Linear regression model
        """
        predictions = self.model.predict(self.x_test)
        mse = mean_squared_error(self.y_test , predictions)
        return mse
    
class RandomForestModel(DataProcessor):
    """
    Derived class for Random Forest model
    """
    def __init__(self, data: pd.DataFrame, target_column: str , n_estimators : int = 100):
        super().__init__(data, target_column)
        self.model = RandomForestRegressor(n_estimators=n_estimators , random_state=42)
        
    def train_model(self):
        """
        train the random forest model
        """
        self.model.fit(self.x_train , self.y_train)
    
    # Method Overriding
    def evaluate_model(self):
        """
        evaluate random forest model
        """
        predictions = self.model.predict(self.x_test)
        mse = mean_squared_error(self.y_test , predictions)
        return mse 

# Example usage 
if __name__ == "__main__": 
    # Sample DataFrame 
    df = pd.DataFrame({ 'feature1': [5, 7, 8, 9, 6, 4, 5, 3], 
                       'feature2': [15, 17, 18, 19, 16, 14, 15, 13], 
                       'feature3': [25, 27, 28, 29, 26, 24, 25, 23], 
                       'target': [50, 70, 80, 90, 60, 40, 50, 30] })
    
    #Linear regression model 
    lr_model = LinearRegressionModel(df , 'target')
    lr_model.process_data()
    lr_model.split_data()
    lr_model.standardize_data()
    lr_model.train_model()
    lr_mse = lr_model.evaluate_model()
    print(f"Linear Regression model MSE : {lr_mse}")
    
    #Random forest regression model 
    rf_model = RandomForestModel(df , 'target')
    rf_model.process_data()
    rf_model.split_data()
    rf_model.standardize_data()
    rf_model.train_model()
    rf_mse = rf_model.evaluate_model()
    print(f"Random foresrt mse : {rf_mse}")
    
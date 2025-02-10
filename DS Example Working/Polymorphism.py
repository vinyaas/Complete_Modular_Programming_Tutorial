import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

class DataModel:
    """
    Base class for data models.
    """
    def __init__(self, data: pd.DataFrame, target_column: str):
        self.data = data
        self.target_column = target_column
        self.features = data.drop(columns=[target_column])
        self.target = data[target_column]

    def preprocess_data(self, scale: bool = False):
        """
        Method overloading example: Preprocess data with optional scaling.
        """
        if scale:
            scaler = StandardScaler()
            self.features = scaler.fit_transform(self.features)
    
    def train_test_split(self, test_size: float = 0.2):
        """
        Split the data into training and testing sets.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features, self.target, test_size=test_size, random_state=42
        )
    
    def train_model(self):
        """
        Method to train the model. To be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def evaluate_model(self):
        """
        Evaluate the model performance.
        """
        predictions = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)
        return mse

class LinearRegressionModel(DataModel):
    """
    Linear Regression Model.
    """
    def train_model(self):
        """
        Method overriding example: Train Linear Regression model.
        """
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

class DecisionTreeModel(DataModel):
    """
    Decision Tree Model.
    """
    def train_model(self):
        """
        Method overriding example: Train Decision Tree model.
        """
        self.model = DecisionTreeRegressor()
        self.model.fit(self.X_train, self.y_train)

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    df = pd.DataFrame({
        'feature1': [5, 7, 8, 9, 6, 4, 5, 3],
        'feature2': [15, 17, 18, 19, 16, 14, 15, 13],
        'feature3': [25, 27, 28, 29, 26, 24, 25, 23],
        'target': [50, 70, 80, 90, 60, 40, 50, 30]
    })

    # Process the data
    lr_model = LinearRegressionModel(df, 'target')
    lr_model.preprocess_data(scale=True)  # Using method overloading with optional scaling
    lr_model.train_test_split()
    lr_model.train_model()  # Using method overriding to train the model
    lr_mse = lr_model.evaluate_model()
    print(f"Linear Regression Model MSE: {lr_mse}")

    dt_model = DecisionTreeModel(df, 'target')
    dt_model.preprocess_data()  # Using method overloading without scaling
    dt_model.train_test_split()
    dt_model.train_model()  # Using method overriding to train the model
    dt_mse = dt_model.evaluate_model()
    print(f"Decision Tree Model MSE: {dt_mse}")

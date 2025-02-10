# Class Methods in Data Science Projects

# 1. Managing Configuration Settings:
# Class methods can be used to update and access configuration settings that are shared across the entire project.
class Config:
    settings = {}

    @classmethod
    def update_setting(cls, key, value):
        cls.settings[key] = value

    @classmethod
    def get_setting(cls, key):
        return cls.settings.get(key)

# Usage:
Config.update_setting('learning_rate', 0.01)
print(Config.get_setting('learning_rate'))  # Output: 0.01

# 2. Alternative Constructors:
# Class methods can provide alternative ways to create instances of data processing or model classes, such as from different data sources.
class DataProcessor:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv(cls, file_path):
        data = pd.read_csv(file_path)
        return cls(data)

    @classmethod
    def from_json(cls, file_path):
        data = pd.read_json(file_path)
        return cls(data)

# Usage:
processor_csv = DataProcessor.from_csv('data.csv')
processor_json = DataProcessor.from_json('data.json')

# 3. Tracking Instances:
# Class methods can keep track of the number of instances of a class, which is useful for monitoring resource usage.
class Model:
    instance_count = 0

    def __init__(self, model_type):
        self.model_type = model_type
        Model.instance_count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

# Usage:
model1 = Model('Linear Regression')
model2 = Model('Decision Tree')
print(Model.get_instance_count())  # Output: 2

# 4. Preprocessing Pipelines:
# Class methods can define and manage preprocessing steps that are applied uniformly across different datasets.
class PreprocessingPipeline:
    steps = []

    @classmethod
    def add_step(cls, step_function):
        cls.steps.append(step_function)

    @classmethod
    def execute_pipeline(cls, data):
        for step in cls.steps:
            data = step(data)
        return data

# Usage:
def normalize(data):
    return data / data.max()

def remove_nulls(data):
    return data.dropna()

PreprocessingPipeline.add_step(normalize)
PreprocessingPipeline.add_step(remove_nulls)

data = pd.DataFrame([1, 2, None, 4])
clean_data = PreprocessingPipeline.execute_pipeline(data)
print(clean_data)

# 5. Shared Resource Management:
# Class methods can manage shared resources such as database connections, ensuring they are used efficiently.
class DatabaseConnection:
    connection_pool = []

    @classmethod
    def get_connection(cls):
        if cls.connection_pool:
            return cls.connection_pool.pop()
        else:
            return cls.create_new_connection()

    @classmethod
    def release_connection(cls, connection):
        cls.connection_pool.append(connection)

    @classmethod
    def create_new_connection(cls):
        # Simulating a new database connection creation
        return "New Database Connection"

# Usage:
conn1 = DatabaseConnection.get_connection()
print(conn1)  # Output: New Database Connection
DatabaseConnection.release_connection(conn1)

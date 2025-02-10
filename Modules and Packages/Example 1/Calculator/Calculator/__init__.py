from Calculator.arithmetic import Arithmetic
from Calculator.geometry import Geometry

# __init__.py File - Importance and Advantages

# The __init__.py file is an essential component in Python packages. It serves several purposes
# and offers numerous benefits. Below are the key points explaining its importance and advantages.

# 1. Package Initialization:
#    - The __init__.py file is executed when a package is imported.
#    - It allows you to initialize the package, set up any necessary variables, 
#      and perform package-level imports.

# 2. Namespace Declaration:
#    - It marks a directory as a Python package directory.
#    - Without an __init__.py file, Python may not recognize the directory as part of a package,
#      especially in older versions of Python (prior to Python 3.3).

# 3. Simplified Imports:
#    - The __init__.py file can be used to simplify import statements.
#    - By importing submodules and functions in __init__.py, you can make them
#      directly accessible from the package level.

# 4. Code Organization:
#    - Helps in organizing and structuring code within a package.
#    - Encapsulates related modules and makes it easier to manage and maintain the codebase.

# 5. Custom Package Behavior:
#    - You can define custom behavior for your package by adding package-level code
#      in the __init__.py file.
#    - This includes setting default values, configuring package settings, or 
#      adding utility functions that are accessible from the package level.

# 6. Compatibility:
#    - Ensures compatibility with tools and frameworks that rely on the presence of __init__.py
#      to recognize packages.


# Example with __init__.py:

# Directory Structure:
# project_root/
#     analysis/
#         __init__.py
#         data_preprocessing.py
#         model_training.py
#     main.py

# analysis/__init__.py:
# from analysis.data_preprocessing import preprocess_data
# from analysis.model_training import train_model

# main.py:
# from analysis import preprocess_data, train_model
# data = load_data("data.csv")
# processed_data = preprocess_data(data)
# model = train_model(processed_data)

# Without __init__.py:

# Directory Structure:
# project_root/
#     analysis/
#         data_preprocessing.py
#         model_training.py
#     main.py

# main.py:
# # Without __init__.py, you need to import from each module explicitly
# from analysis.data_preprocessing import preprocess_data
# from analysis.model_training import train_model
# data = load_data("data.csv")
# processed_data = preprocess_data(data)
# model = train_model(processed_data)

# Summary:
# Using __init__.py simplifies imports, organizes code better, and allows for package initialization.
# Without __init__.py, explicit imports are needed, which can lead to longer, less organized import statement

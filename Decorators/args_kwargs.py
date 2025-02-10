#----------------------------args and kwargs---------------------------------------------------
    # *args: These are the positional arguments you pass to a function.
    # Think of them as the main inputs or parameters that the function will work with.
    
    # **kwargs: These are the keyword arguments.
    # They act like settings or options that modify or control how the function operates on the *args.
    
    # Note : use args and kwargs in your function when you dont know exactly how many arguments and parameters will be passed on to the function.
    # Note : In a DS project use them for utility functions such as logging , exception handling etc .
    

def add(*args , **kwargs):
    total = sum(args)
    display_result = kwargs.get('display' , False) # kwargs is a dictionary containing {'display': True}
    if display_result:
        print(f"Total is {total}")
    return total

result = add(1,2,3,4,5  , display = True) # only if display is set true it will display the result

# What Happens Here: 
# # 1. *args collects the numbers (1, 2, 3, 4, 5) into a tuple. 
# # 2. **kwargs collects the display setting (display=True) into a dictionary. 
# # 3. The function sums the numbers and prints the total if the display setting is True.

#--------------------------------------------------------------------------------------------------

def sum_numbers(*args , **kwargs):
    
    total = sum(args)
    
    #check for precision and rounding settings 
    precision = kwargs.get('precision' , 2) # default to two decimals if not mentioned 
    rounding = kwargs.get('rounding' , 'none') # Default to none if rounding isnt specified
    
    if rounding == 'up':
        total = round(total , precision)
    elif rounding == 'down':
        total = int(total * (10**precision)) / (10**precision)
    else:
        total = round(total , precision)
        
    display_result = kwargs.get('display' , True)
    if display_result:
        print(f"Total is : {total}")
        
    return total

result = sum_numbers( 1.234 , 3.245 , 3.456, 4.567, 5.678 , precision = 1 , rounding = 'down' , display = True)

# What Happens Here:
# 1. *args collects the numbers (1.234, 2.345, 3.456, 4.567, 5.678) into a tuple.
# 2. **kwargs collects the settings (precision=2, rounding='down', display=True) into a dictionary.
# 3. The function calculates the sum of the numbers and applies the specified precision and rounding settings.
# 4. The function prints the result if the display setting is True.

#--------------------------------------------------------------------------------------------------------------------------
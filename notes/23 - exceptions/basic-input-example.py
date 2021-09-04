#-----------------------------------------------------------------------------
# Name:        Catching Exceptions (try-except.py)
# Purpose:     To provide example of a simple input loop using try-catch
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-March-2021
#-----------------------------------------------------------------------------

while True: #Start an infinite loop
    
    value = input('Enter a number between -100 and 100: ') #Get a value from the user
    
    try:
        value = int(value)   #Convert the value to an int
        
    except Exception as e:
        print(f'Something went wrong: {e}') #You should probably add a nicer error message
       

    else:
        #No exception was thrown, so break out of the infinite loop
        break
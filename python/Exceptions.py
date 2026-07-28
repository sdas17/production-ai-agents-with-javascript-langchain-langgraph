# Exceptions
import sys

x =int(input('enter your x:'))
y=int(input('enter your y:'))


try:
    result = x / y
    # ZeroDivisionError
    #ValueeError
    #ZeroDivisionError
    
except ValueError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)


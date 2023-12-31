"""
Resolution example:

def resolution_example(argument):
    try:
        {What the function would usually do}
    except:
        {Exception}
    else:
        ... etc.
"""

def division(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Arguments must be numbers")
    except ZeroDivisionError:
        print("Second argument must not be zero")
    else:
        pass

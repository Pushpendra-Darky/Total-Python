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

def sum_num(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Unexpected error")
    else:
        pass

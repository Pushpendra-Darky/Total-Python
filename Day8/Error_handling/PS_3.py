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

def open_file(file_name):
    try:
        file = open(file_name)
        print("Opening successfully")
    except FileNotFoundError:
        print("The file was not found")
    except Exception:
        print("Unknown error")
    finally:
        print("Ending execution")

'''
import re

def check_email(email):
    pattern = ".+@+'.com'"  # example @ domain . com
    if re.match(pattern,email):
        print("Ok")
    else:
        print("The email address is incorrect")'
'''

import re
def check_email(email):
    pattern = r'@\w+\.com'
    check = re.search(pattern,email)
    if check:
        print("Ok")
    else:
        print("The email address is incorrect")

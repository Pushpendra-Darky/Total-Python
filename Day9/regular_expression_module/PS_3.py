import re

def check_pc(pc):
    pattern = r'\w\w\d\d\d\d'
    if re.search(pattern,pc):
        print("Ok")
    else:
        print("The zip code entered is not correct")

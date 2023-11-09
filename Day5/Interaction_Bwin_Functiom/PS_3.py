

from random import *

def toss_coin():
    res = (["Heads","Tails"])
    result = choice(res)
    return result

def luck(toss_res,list1):
    if toss_res == "Tails":
        print("List will self-destruct")
        return []
    elif toss_res == "Heads":
        print("List was saved")
        return list1
    else:
        pass


secret_codes = ([1,2,3,4])
res1 = toss_coin()
res2 = luck(res1,secret_codes)

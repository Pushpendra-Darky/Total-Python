from random import *

def roll_result(dice1,dice2):
    sum_dice = dice1+dice2

    if sum_dice <=6:
        print(f"The sum of your dice is {sum_dice}. Unfortunate")
    elif sum_dice >6 and sum_dice<10:
        print(f"The sum of your dice is {sum_dice}. You have a good chance")
    elif sum_dice >=10:
        print("The sum of your dice is {sum_dice}. It looks like a winning roll")
    else:
        pass

def throw_dice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1,dice2


val1,val2 = throw_dice()
roll_result(val1,val2)

''''
import random
secret_codes = [1,2,15,7,2,8]
def toss_coin():
    result = random.choice(["Heads", "Tails"])
    return result
def luck(coin, some_list):
    if coin == "Tails":
        print("List will self-destruct")
        return []
    elif coin == "Heads":
        print("List was saved")
        return some_list
'''

from random import *
secret_number = 69
random_number = 0
max_chance = 8
no_tries =0
name = input("Enter your name\n")
print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it.What number do you think it is?")

while( no_tries < max_chance):
    number = int(input())
    no_tries +=1
    if number<1 and number>100:
        print("NOT IN RANGE")
    elif number<secret_number:
        print("LOWER TO SECRET NUMBER")
    elif number>secret_number:
        print("HIGHER TO SECRET NUMBER")
    elif number==secret_number:
        print(f"Hurray! You have Won in {no_tries} attempts")
    elif number==secret_number and no_tries==1:
        print("You have won in your first attemp.Do you want to play again:(Y?N)")
        ch = chr(input())
        if ch=='Y':
            no_tries = 0
            print("Enter the number")
            number = int(input())
        else:
            print("Thank You!\n")
            break;
    else:
        print("Sorry You Tried all the attempts!!!!!!!!!")
        break;



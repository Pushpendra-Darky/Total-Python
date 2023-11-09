number = 50

while number>0:
    if number%5==0:
        print(number)
        number -=1
    else:
        number -=1
        if number ==0:
            print(number)
        else:
            continue

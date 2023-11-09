def function(*args):
    count =0
    for arg in args:
        if arg==0:
            count +=1
            if count==2:
                return True
            else:
                pass
        else:
            pass
    return False

numbers = function(1,0,0,1,5)
print(numbers)


'''
def neighboring_zeros(*args):
    counter =0
    if counter +1= len(args):
    return False
    elif args[counter] ==0 and args[counter+1]==0:
    return True
    else:
        counter +=1
   return False

print(neighboring_zeros(2,1,0,1,0,0))
'''

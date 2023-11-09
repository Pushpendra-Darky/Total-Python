

def return_distincts(*args):
    for num in args:
        sum += num

    if sum >15:
        return max(args)
    elif sum<10:
        return min(args)
    elif sum >= 10 and sum <=15:
        return (sum-(max(args)+min(args)))

'''
def return_diffrent_values(a,b,c):
    a_sum = a+b+c
    a_list = [a,b,c]
    
    if a_sum >15:
        return max(a_list)
    elif a_sum<10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]
    
print(return_diffrent_values(20,5,7))
        '''

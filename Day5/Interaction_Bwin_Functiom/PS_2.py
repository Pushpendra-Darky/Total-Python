def reduce_list(numbers):
    dup_rem = list(set(numbers))
    #return dup_rem
    max_v = max(dup_rem)
    dup_rem.remove(max_v)
    return dup_rem


def average(l):
    sum_v =0.0
    avg =0.0
    count =0
    for n in l:
        count +=1
        sum_v +=n

    return sum_v/count

numbers = ([1,2,3,15,7,2])
list2 = reduce_list(numbers)
result = average(list2)

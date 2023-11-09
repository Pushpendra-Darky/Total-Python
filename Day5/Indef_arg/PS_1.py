def sum_squares(*args):
    sum_v =0
    for arg in args:
        arg *= arg
        sum_v += arg
    return sum_v

result = sum_squares(1,2,3)
print(result)

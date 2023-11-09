def absolute_sum(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total

result = absolute_sum(-5, 10, -3, 7, -2)
print(result)

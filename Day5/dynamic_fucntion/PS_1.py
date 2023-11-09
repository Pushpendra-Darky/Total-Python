def all_positives(numbers):
    for n in numbers:
        if n<0:
            return False
        else:
            pass
    return True

numbers = ([1,2,-3])
'''result = all_positives(numbers)
print(result)

def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num
practice_generator = infinite_sequence()


'''
def generator():
    for n in range(1,10):
        yield n
    
    
practice_generator = generator()
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))


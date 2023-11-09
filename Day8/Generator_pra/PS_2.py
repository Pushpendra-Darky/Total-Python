def sevens():
    num = 1
    while True:
        yield 7*num
        num += 1
practice_generator = sevens()


'''
def generator():
    for n in range(1,10):
        yield n*7
    
    
practice_generator = generator()
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))

'''

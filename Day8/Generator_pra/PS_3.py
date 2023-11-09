'''
def my_gen():
    n=3
    while n>0:
        yield f"You have {n} lives left"
        n-=1
    yield "Game Over"

lose_live = my_gen()
print(next(lose_live))
print(next(lose_live))
print(next(lose_live))
print(next(lose_live))
'''
def message():
    x = "You have 3 lives left"
    yield x
    x = "You have 2 lives left"
    yield x
    x = "You have 1 live left"
    yield x
    x = "Game Over"
    yield x
lose_live = message()

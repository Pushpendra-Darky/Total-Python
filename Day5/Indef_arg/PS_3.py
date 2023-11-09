def personal_numbers(name,*args):
    sum_numbers = sum(args)
    return (f"{name}, the sum of your numbers is {sum_numbers}")

message = personal_numbers("DARKY",1,2,3,4,5)
print(message)

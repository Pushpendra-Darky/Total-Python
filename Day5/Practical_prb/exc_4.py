

def count_primes(*args):
    val =0
    count =0
    for arg in args:
        val +=1
        if arg%val==0:
            count +=1
        else:
            pass
    if count==2:
        return 1,
    else:
        return 0
'''
def count_prime_number(number):
    prime_number = [2]
    iteration = 3

    if number <2:
        return 0

    while iteration <=number:
        for n in range(3,iteration,2):
            if iteration %n ==0:
                iteration +=2
                break
            else:
                prime_number.append(iteration)
                iteration +=2

        print(prime_number)
        return len(prime_number)

print(count_prime_number(50))
'''





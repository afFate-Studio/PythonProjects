def prime_checker(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

n = int(input('Check this number: ')) 
isPrime = prime_checker(number=n)

if isPrime:
    print(f'You number {n} is a prime number.')
else:
    print(f'Your number {n} is not a prime number.')
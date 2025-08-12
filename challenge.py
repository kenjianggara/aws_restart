import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(1, 251):
    if is_prime(num):
        primes.append(num)

with open('results.txt', 'w') as file:
    for prime in primes:
        file.write(f"{prime}\n")

print("Prime numbers between 1 and 250 have been written to results.txt")

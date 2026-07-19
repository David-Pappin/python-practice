
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
count = 0
num = 0
primes = []

while count < 100:
    if is_prime(num):
        primes.append(num)
        count +=1
    num += 1


for prime in primes:
    print(prime)

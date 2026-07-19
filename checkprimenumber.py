# # a prime number is ay number that is greater than 1 and  divisible by 2 and the number itslef with no other divisor
# #define the prime, name it and pass the argument which will be the number to check
# since a prime has to be greater than 1 you need to ensure anynumber less than or equal to 1 is immedietly not a prime
#you will then have to check the range from 2 to the nuber -1 since we alredy know that any numberis divisible by itself
#then you check for each iterated no. if you take the modulo of that to the number we are checking and its remainder is 0
#then that means it is not a prime so it returns false else if the range of numbers does not leave a remainder of 0 which means 
#the range of numbers is not divisible by the number we check then that number is a prime.

# to begin with i will set a counter to 0 and a list collection to hold our primes, also a num varfiable that will be our counter for the numbers we check.
# starting from 2 with the num since we have already i dentified that 2 is the smallest prime number 
#it is faster and i dont need to modify it 
#first of all, you need to start with the while loop since you dont have a fixed number you are iterating over, in this case the code runs till the prime 
# counter reaches 100
# then next we check if our initial num variable which is two is a prime then we add it to our list
#then we increment num and the counter and the loop runs till we get our first 100 primes
#then we print


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



count = 0
num = 2
primes = []
while count < 100:
    if isPrime(num):
        primes.append(num)
        count +=1
    num +=1
    

for i in primes:
    print(i)


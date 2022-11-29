'''
Problem ID:
PE0010

Problem Title:
Summation of primes

Problem Description:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Problem Solution:

'''
import time

def isPrime(number):
    result = True
    divisor = 2
    while divisor != number:        
        if number%divisor == 0:
            result = False
            break
        divisor += 1
    return result

def solution(number):
    result = 0
    for k in range(2,number):
        print(k)
        if isPrime(k):
            result+=k
    return result

timer=time.time()
print(solution(10))
print(f'It took {round(time.time()-timer,4)} secs')
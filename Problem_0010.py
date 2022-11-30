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
from primality import primality as prim

def solution(number):
    result = 0
    while number>1:
        if prim.isprime(number):
            result += number
        number -= 1
    return result

timer=time.time()
print(solution(2*10**6))
print(f'It took {round(time.time()-timer,4)} secs')
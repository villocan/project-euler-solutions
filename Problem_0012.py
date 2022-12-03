'''
Problem ID:
PE0012

Problem Title:
Highly divisible triangular number

Problem Description:
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?

Problem Solution:
76576500
'''
import time
from primality import primality as prim
#prim.isprime(number) or number%2!=0 or number%3!=0 or number%4!=0 or number%5!=0 or number%6!=0 or number%7!=0:

def isCandidate(number,min_n):
    result = False
    n = 0
    k = 0
    n_list = []
    while number > 2:
        if k>1:
            break
        if number%prim.nthprime(n) == 0:
            k = 0
            number /= prim.nthprime(n)
            n_list.append(prim.nthprime(n))
        else:
            n += 1
            k += 1
    if len(n_list)>=min_n:
        result = True
    return result

def triangNumber(n):
    return round((n**2+n)/2)

def findDivisors(number):
    d_size = 2
#    d_list = [1,number]
    for k in range(2,number):
        if number%k==0:
#            d_list.append(k)
            d_size += 1
    return d_size

def solution(min_divisors):
    result = 0
    divisors = 0
    n = 1
    while divisors<min_divisors:
        n += 1
        result = triangNumber(n)
        if isCandidate(result,11):
            divisors = findDivisors(result)
        print(n,result,divisors)
    return result

timer=time.time()
print(solution(500))
print(f'It took {round(time.time()-timer,4)} secs')
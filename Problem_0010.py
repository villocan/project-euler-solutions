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

def isPrime(N):
    multiples=0
    for n in range(1,N):
        if N%(N-n)==0:
            multiples+=1
        if multiples>1:
            return False
    return True

def solution(number):
    result = 0
    for k in range(2,number):
        print(k)
        if isPrime(k):
            result+=k
    return result

print(solution(2*10**6))
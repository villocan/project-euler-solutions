'''
Problem ID:
PE0003

Problem Title:
Largest prime factor

Problem Description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Problem Solution:
6857
'''

def isPrime(N):
    multiples=0
    for n in range(1,N):
        if N%(N-n)==0:
            multiples+=1
        if multiples>1:
            return False
    return True

def solution(N):
    total=1    #
    factor=0   #
    while total<N:
        factor+=1
        while not(isPrime(factor)):
            factor+=1
        if N%factor==0:
            total*=factor
    return factor

print(solution(600851475143))
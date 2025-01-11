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

def isPrime(n):
    for k in range(2,n):
        if n%k == 0:
            return False
    return True
        

def solution(n):
    result = n
    last = 1
    factor = 1
    while result != 1:
        factor += 1
        if isPrime(factor) and result%factor == 0:
            last = factor
            result = result/factor
    return last

print(solution(13195))
print(solution(600851475143))
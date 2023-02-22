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
import random

def isPrime(n, k=5):
    # Si n es 2 o 3, entonces es primo
    if n == 2 or n == 3:
        return True
    # Si n es par, entonces no es primo
    if n % 2 == 0:
        return False
    
    # Encontrar d y r tal que n-1 = 2^r * d, donde d es impar
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Realizar el test de Miller-Rabin k veces
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    
    # Si pasa todas las iteraciones, es probable que sea primo
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
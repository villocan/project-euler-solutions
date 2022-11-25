'''
Problem ID:
PE0007

Problem Title:
10001st prime

Problem Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

Problem Solution:
104743
'''

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
    result = 1
    count = 0
    while count != number:
        result +=1
        if isPrime(result):
            count += 1
    return result

print(solution(10001))
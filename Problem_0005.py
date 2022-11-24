'''
Problem ID:
PE0005

Problem Title:
Smallest multiple

Problem Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Problem Solution:
232792560
'''

def isMultiple(x,y):
    result = False
    if x%y == 0:
        result = True
    return result

def solution():
    result = 1
    for k in range(1,1+20):
        if not(isMultiple(result,k)):
            if isMultiple(2*result,k):
                result *= 2
            elif isMultiple(3*result,k):
                result *= 3
            elif isMultiple(5*result,k):
                result *= 5
            else:
                result *= k
    return result

print(solution())
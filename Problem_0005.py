'''
Problem ID:
0005

Problem Title:
Smallest multiple

Problem Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Problem Solution:

'''

def isMultiple(x,y):
    result = False
    if x%y == 0:
        result = True
    return result

def solution():
    result = 2500
    try_again = True
    while try_again:
        try_again = False
        result += 1
        for k in range(1,21):
            if not(isMultiple(result,k)):
                try_again = True
    return result

print(solution())
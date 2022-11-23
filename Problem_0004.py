'''
Problem ID:
0004

Problem Title:
Largest palindrome product

Problem Description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Problem Solution:
906609
'''

def isPalindromic(x):
    x=str(x)
    result = False
    if x == x[::-1]:
        result = True
    return result

def solution():
    test = 0
    keep = 0
    for k in range(100,1000):
        for l in range(100,1000):
            test = k*l
            if isPalindromic(test) and test>keep:
                keep = test
    return keep


print(solution())
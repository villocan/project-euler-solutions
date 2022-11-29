'''
Problem ID:
PE0009

Problem Title:
Special Pythagorean triplet

Problem Description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Problem Solution:

'''

def solution():
    a=1
    b=1
    while a+b+(a**2+b**2)**0.5 != 1000:
        a+=1
        if a==1000:
            b+=1
            a=1
        print(a+b+(a**2+b**2)**0.5)
    return a*b*(a**2+b**2)**0.5

print(solution())
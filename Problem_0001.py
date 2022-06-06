'''
Problem ID:
0001

Problem Title:
Multiples of 3 or 5

Problem Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Problem Solution:
233168
'''

def solution(max):
    total=0
    for k in range(1,max):
        if k%3==0 or k%5==0:
            total+=k
    return total

print(solution(1000))
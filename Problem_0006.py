'''
Problem ID:
PE0006

Problem Title:
Sum square difference

Problem Description:
The sum of the squares of the first ten natural numbers is,
1**2+2**2+...+10**2=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)**10=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Problem Solution:
25164150
'''

def solution(max):
    result = 0
    a = 0
    for number in range(1,1+max):
        result -= number**2
        a += number
    result += a**2
    return result

print(solution(100))
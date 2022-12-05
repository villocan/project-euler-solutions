'''
Problem ID:
PE0014

Problem Title:
Longest Collatz sequence

Problem Description:
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Problem Solution:

'''
import time

def CollatzSequence(n):
    n_sequence = []
    while n != 1:
        n_sequence.append(round(n))
        if n%2==0:
            n /= 2
        else:
            n = 3*n+1
    n_sequence.append(1)
    return n_sequence

def solution(max_number):
    result = 0
    result_size = 0
    n = 0
    while n < max_number:
        n += 1
        n_sequence = CollatzSequence(n)
        if result_size < len(n_sequence):
            result_size = len(n_sequence)
            result = n
        print(n,result)
    return result

timer=time.time()
print(solution(10**6))
print(f'It took {round(time.time()-timer,4)} secs')
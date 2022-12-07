'''
Problem ID:
PE0015

Problem Title:
Lattice paths

Problem Description:
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?

Problem Solution:

'''
import time

def solution(n):
    result = 0
    P=[1,1]
    S=2*n
    return result

timer=time.time()
print(solution(2))
print(f'It took {round(time.time()-timer,4)} secs')
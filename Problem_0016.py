'''
Problem ID:
PE0016

Problem Title:
Power digit sum

Problem Description:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Problem Solution:
1366
'''
import time

def sum_digits(n):
  digits = str(n)
  sum = 0
  for digit in digits:
    sum += int(digit)
  return sum

def solution():
    result = 0
    n = 2 ** 1000
    result = sum_digits(n)
    return result

timer=time.time()
print(solution())
print(f'It took {round(time.time()-timer,4)} secs')
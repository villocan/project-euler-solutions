'''
Problem ID:
PE0100

Problem Title:
Arranged probability

Problem Description:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

Problem Solution:

'''

def solution():
    # blue_discs = round(0.5*(1+(1+2*(10**12)*(10**12-1))**0.5))
    # red_discs = 10**12 - blue_discs
    blue_discs = 0
    red_discs = 0
    discs = 1000000002605
    err = 1
    while err != 0:
        K = discs
        A = 2
        B = 2-4*K
        C = K**2-K
        red_discs = (-B-(B**2-4*A*C)**0.5)/(2*A)
        blue_discs = discs - red_discs
        err = abs(red_discs-round(red_discs))
        discs += 1
    return blue_discs

print(solution())
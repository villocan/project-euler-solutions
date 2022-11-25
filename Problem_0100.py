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
    blue_discs = 1+707106849950
    red_discs = 10**12 - blue_discs
    err = 1
    while err != 0:
        prob = (blue_discs/(blue_discs+red_discs))*((blue_discs-1)/(blue_discs+red_discs-1))
        if prob < 0.5:
            blue_discs += 1
        elif prob > 0.5:
            red_discs += 1
        err = 200*abs(prob-0.5)
        print(blue_discs,red_discs)
    result = blue_discs
    return result

print(solution())
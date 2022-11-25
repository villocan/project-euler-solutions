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
    result = round(0.5*(1+(1+2*(10**12)*(10**12-1))**0.5))
    total = 10**12
    prob = (result/total)*((result-1)/(total-1))
    while prob != 0.5:
        if prob > 0.5:
            total += 1
        elif prob < 0.5:
            total += 1
            result += 1
        prob = (result/total)*((result-1)/(total-1))
        print(result,total,prob)
    return result

print(solution())
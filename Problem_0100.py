'''
Problem ID:
PE0100

Problem Title:
Arranged probability

Problem Description:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random,
it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

Problem Solution:
756872327473
'''

def solution(min_discs,target_prob):
    blue_discs = round(0.5+(0.25+target_prob*min_discs*(min_discs-1))**0.5)
    red_discs = min_discs-blue_discs
    prob = 0
    while blue_discs+red_discs<min_discs or prob!=target_prob:
        if prob < target_prob:
            blue_discs += 1
        else:
            red_discs += 1
        prob = blue_discs*(blue_discs-1)/(blue_discs+red_discs)/(blue_discs+red_discs-1)
        print(prob,blue_discs,red_discs)
    return blue_discs, red_discs

print(solution(10**12,0.5))
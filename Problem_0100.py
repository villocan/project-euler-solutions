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

def isPrime(number):
    result = True
    divisor = 2
    while divisor != number:        
        if number%divisor == 0:
            result = False
            break
        divisor += 1
    return result

def findPrimes(number):
    result = []
    divisor = 2
    while number != 1:
        if isPrime(divisor):
            if number%divisor == 0:
                result.append(divisor)
                number /= divisor
            else:
                divisor += 1
        else:
            divisor += 1
        if abs(number) > 1 and abs(number) < 2:
            result = 'error'
            break
    result.sort(reverse=True)
    return result

def solution(min_discs):
    blue_discs = 756872327472
    red_discs = 10**12-756872327472
    prob = 1/6
    while blue_discs+red_discs<min_discs or den.pop()!=2 or den!=num:
        if prob < 0.5:
            blue_discs += 1
        else:
            red_discs += 1
        num = findPrimes(blue_discs*(blue_discs-1))
        den = findPrimes((blue_discs+red_discs)*(blue_discs+red_discs-1))
        prob = round(blue_discs*(blue_discs-1)/(blue_discs+red_discs)/(blue_discs+red_discs-1),10)
        print(prob,blue_discs,red_discs,num,den)
    return blue_discs

print(solution(10**12))
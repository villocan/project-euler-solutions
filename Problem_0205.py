'''
Problem ID:
PE0205

Problem Title:
Dice Game

Problem Description:
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

Problem Solution:

'''

class Person:
    def __init__(self, dices, faces_per_dice):
        self.dices = dices
        self.faces_per_dice = faces_per_dice
        self.cardinal = faces_per_dice**dices
        self.combinations = []
        self.totals = []
        self.filtered = []
        row = [1]*dices
        row[0] = 0
        for k1 in range (0,self.cardinal):
            for k2 in range(0,dices):
                if k2==0:
                    row[0]+=1
                if row[k2]>faces_per_dice:
                    row[k2]=1
                    row[k2+1]+=1
            self.combinations.append(row.copy())
            self.totals.append(sum(row))

Peter = Person(9,4)
Colin = Person(6,6)

def solution():
    result = 0
    for value1 in Peter.totals:
        for value2 in Colin.totals:
            if value1 > value2:
                result += 1
    result *= 1/(Colin.cardinal*Peter.cardinal)
    return round(result,7)

print(solution())
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
    col = 0
    row = [1]
    for k1 in range(1,dices):
        row.append(1)
    for k2 in range (1,1+self.cardinal):
        self.combinations.append(row)
        row[col]=k2%faces_per_dice+1
        if k2%faces_per_dice+1 == 1:
            col+=1
        if col == faces_per_dice-1:
            col=0
        


  def f1(self):
    return 0

Colin = Person(4,4)
Peter = Person(6,6)

print(Colin.cardinal)
print(Peter.cardinal)

def solution():
    result = 0
    return result

print(solution())
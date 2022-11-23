'''
Problem ID:
0566

Problem Title:
Cake Icing Puzzle

Problem Description:
Adam plays the following game with his birthday cake.
He cuts a piece forming a circular sector of 60 degrees and flips the piece upside down, with the icing on the bottom.
He then rotates the cake by 60 degrees counterclockwise, cuts an adjacent 60 degree piece and flips it upside down.
He keeps repeating this, until after a total of twelve steps, all the icing is back on top.
Amazingly, this works for any piece size, even if the cutting angle is an irrational number: all the icing will be back on top after a finite number of steps.
Now, Adam tries something different: he alternates cutting pieces of size
x=360/9 degrees, y=360/10 degrees and z=360/sqrt(11) degrees.
The first piece he cuts has size x and he flips it. The second has size y and he flips it. The third has size z and he flips it.
He repeats this with pieces of size x, y and z in that order until all the icing is back on top, and discovers he needs 60 flips altogether.
Let F(a, b, c) be the minimum number of piece flips needed to get all the icing back on top for pieces of size 
x=360/a degrees, y=360/b degrees and z=360/sqrt(c) degrees.
Let G(n)=Sum(F(a, b, c),9<=a<b<c<=n), for integers a, b and c.
You are given that F(9, 10, 11) = 60, F(10, 14, 16) = 506, F(15, 16, 17) = 785232.
You are also given G(11) = 60, G(14) = 58020 and G(17) = 1269260.
Find G(53).

Problem Solution:

'''
import time
from turtle import position
start_time = time.time()

class Cake():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.factor=10**3
        self.full=360*self.factor
        self.x=round(self.full/a)
        self.y=round(self.full/b)
        self.z=round(self.full/(c**0.5))        
        self.slices=[]
        for k in range(0,self.full):
            self.slices+=[1]
        self.position=0
        self.slice_buffer=[]
        self.icing_on_top=0
        self.icing_on_bottom=0
    def chopAndFlip(self,size):
        # chop
        old_position=self.position
        if self.position+size<self.full:
            self.slice_buffer=self.slices[self.position:self.position+size]
            self.position+=size
            if self.position==self.full:
                self.position=0
        else:
            self.slice_buffer=self.slices[self.position:self.full]+self.slices[0:size-self.full+self.position]
            self.position=size-self.full+self.position
        # flip
        self.slice_buffer.reverse()
        for index in range(0,len(self.slice_buffer)):
            if self.slice_buffer[index]==0:
                self.slice_buffer[index]=1
            elif self.slice_buffer[index]==1:
                self.slice_buffer[index]=0
        # insert

    def totalize(self):
        self.icing_on_top=100*sum(self.slices)/self.full
        self.icing_on_bottom=100-self.icing_on_top
    def talk(self):
        self.totalize()
        self.chopAndFlip(self.x)
        print(self.icing_on_top,self.icing_on_bottom)

Cake1= Cake(9,10,11)
Cake1.talk()

print("Time: " + str(time.time()-start_time) + " secs")
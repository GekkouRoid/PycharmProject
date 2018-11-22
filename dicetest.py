# Exercise of 9-14

import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        x = random.randint(1, self.sides)
        # print(x)
        return x


dice1 = Dice()
dice1.roll_dice()

dice2 = Dice(10)
seq2 = []

for i in range(10):
    seq2.append(dice2.roll_dice())

print(seq2)

dice3 = Dice(20)
seq3 = []
for i in range(10):
    seq3.append(dice3.roll_dice())

print(seq3)

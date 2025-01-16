import random


class Dice():
    def roll(self):
        roll = (random.randint(1,6), random.randint(1,6))
        return roll
    

dice = Dice()
print(dice.roll())



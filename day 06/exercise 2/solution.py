import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        # If you want to return a tuple, don't need (), just do as below
        return first, second


dice = Dice()
print(dice.roll())
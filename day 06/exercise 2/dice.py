import random

class Dice:
    def roll(self):
        result = random.randint(1,6)
        return result 

result1 = Dice()
result2 = Dice()

print(result1.roll(), result2.roll())
"""Creat a die"""

from random import randint

class Die:
    """Describe a die with 6 sides"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1,self.sides)
        print(number)

my_die_6 = Die()
my_die_6.roll_die()

my_die_10 = Die(10)
my_die_10.roll_die()

my_die_20 = Die(20)
my_die_20.roll_die()
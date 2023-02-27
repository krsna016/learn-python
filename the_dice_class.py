"""This is the Dice class module"""


from random import randint
from time import sleep


class Dice():
    """This class is to roll the n-sided dice"""

    def __init__(self, dice_sides=6):
        """Initialising the attributes for the class 'Dice'"""
        self.sides = dice_sides

    def roll_dice(self, no_times):
        """This method is used to roll the dice"""
        for i in range(1,no_times+1):
            print(f"Rolling time - {i} :",randint(1, self.sides))
            sleep(1)

# Provide no of sides in the Dice() as agrument (optional, default = 6)
dice = Dice(10) # Sides
# Provide number of time the dice to be roll in roll_dice() as argument (Not optional)
dice.roll_dice(10) # Times
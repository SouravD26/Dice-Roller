#-------------------------------------------------------------------------------
# Name:        Sourav Dutta
# Purpose:
#
# Author:      DELL PC
#
# Created:     04-01-2024
#------------------------------------------------------------------------------

import random

# input statement for number of sides
num_sides = int(input("Enter Number of sides: "))

# Loop Condition
while True:
    print("Rolling Dice.....")

# Using random.randint to generate random number of dice
    dice_roll = random.randint(1,num_sides)

    print("Dice Rolled",dice_roll)

# asking user for dice roll
    repeat = input("Roll the Dice again? if yes then type 'y' or 'n' for no: ")

# if the user enter n,the loop will be break
    if repeat == 'n':
        break

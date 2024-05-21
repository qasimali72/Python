# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#importing module for random number generation
import random
#range of the values of a dice
min_val = 1
max_val = 6

#loop rolling through user input
roll_again = "yes"

#loop rolling 
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again. Any input other than yes or y will play angin and 1 will be terminate the loop 
    roll_again = input("Roll the Dices Again?") 
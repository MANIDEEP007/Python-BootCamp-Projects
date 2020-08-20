'''
Dice Simulator
'''

import random #To Generate Random Numbers
choice = 'Y' #Variable to Store Choice of User
print("Dice Simulator")
while choice == 'Y' or choice == 'y': #Checking Choice of User
    #Random Integers - random.randint(a,b)- Inclusive a,b
    number = random.randint(1,6)
    #Print the respective pattern based on the number rolled
    if number == 1:
        print(
            '''
            ==========
            |        |
            |        |
            |    0   |
            |        |
            |        |
            ==========
            '''
            )
    if number == 2:
        print(
            '''
            ==========
            |        |
            |        |
            | 0    0 |
            |        |
            |        |
            ==========
            '''
            )
    if number == 3:
        print(
            '''
            ==========
            |        |
            |    0   |
            |    0   |
            |    0   |
            |        |
            ==========
            '''
            )
    if number == 4:
        print(
            '''
            ==========
            |        |
            | 0    0 |
            |        |
            | 0    0 |
            |        |
            ==========
            '''
            )
    if number == 5:
        print(
            '''
            ==========
            | 0    0 |
            |        |
            |    0   |
            |        |
            | 0    0 |
            ==========
            '''
            )
    
    if number == 6:
        print(
           '''
            ==========
            | 0    0 |
            |        |
            | 0    0 |
            |        |
            | 0    0 |
            ==========
            '''
            )
    #Get the Choice of the User for Next Roll
    choice = input("Press Y to Roll the Dice Again: ")

'''
Dice Simulator
'''

import random #To Generate Random Numbers
import prettytable #To Print the Dices
choice = 'Y' #Variable to Store Choice of User
print("Dice Simulator")

#Patterns
one ='''
==========
|        |
|        |
|    0   |
|        |
|        |
==========
'''
two = '''
==========
|        |
|        |
| 0    0 |
|        |
|        |
==========
'''
three = '''
==========
|        |
|    0   |
|    0   |
|    0   |
|        |
==========
'''
four = '''
==========
|        |
| 0    0 |
|        |
| 0    0 |
|        |
==========
'''
five = '''
==========
| 0    0 |
|        |
|    0   |
|        |
| 0    0 |
==========
'''
six = '''
==========
| 0    0 |
|        |
| 0    0 |
|        |
| 0    0 |
==========
'''
#Number to Pattern Mapping
dice = {
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six,
    }

while choice == 'Y' or choice == 'y': #Checking Choice of User
    #Random Integers - random.randint(a,b)- Inclusive a,b
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    table = prettytable.PrettyTable(
        border=False,
        vrules=prettytable.NONE,
        header=False
        )
    table.add_row([dice[number1],dice[number2]])
    print(table)
    #Get the Choice of the User for Next Roll
    choice = input("Press Y to Roll the Dice Again: ")

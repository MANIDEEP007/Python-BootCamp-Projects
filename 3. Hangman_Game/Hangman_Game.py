import random

nine    = "-------"
eight   = "-------\n" +\
          "   0   "
seven   = "-------\n" +\
          "   0   \n" +\
          "   |   \n"
six     = "-------\n" +\
          "   0   \n" +\
          "   |   \n" +\
          "  /    "
five    = "-------\n" +\
          "   0   \n" +\
          "   |   \n" +\
          "  / \  \n"
four    = "-------\n" +\
          r"  \0   " + "\n" +\
          "   |   \n" +\
          "  / \  \n"
three   = "-------\n" +\
          r"  \0/  " + "\n" +\
          "   |   \n" +\
          "  / \  \n"
two     = "-------\n" +\
          r"  \0/| " + "\n" +\
          "   |   \n" +\
          "  / \  \n"
one     = "-------\n" +\
          r"  \0_|/" + "\n" +\
          "   |   \n" +\
          "  / \  \n"
zero    = "-------\n" +\
          r"   0_/ " + "\n" +\
          "  /|\  \n" +\
          "  / \  \n"

#Dictionary to print Hangman based on the Attempts
dict_turns = {
    0:zero,
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six,
    7:seven,
    8:eight,
    9:nine,
    }

def hangman_game():
    #List of Animals
    animals = [
        "rhino",
        "tiger",
        "parrot",
        "monkey",
        "lion",
        "tiger",
        "leopard",
        "cheetah",
        "donkey",
        "sheep",
        ]

    #Valid Choices
    choices = "abcdefghijklmnopqrstuvwxyz"

    #Total Number of Attempts
    turns = 10
    
    #Guesses Made by User
    letters_guessed = ""
    
    #Take Random Animal Word
    guess_word = random.choice(animals)

    #Check Guess Word is selected or not
    while len(guess_word) > 0:
        #Progres of the User
        progress = ""

        #Print the Progress of the User
        for letter in guess_word:
            if letter in letters_guessed:
                progress += letter
            else:
                progress += "_" +" "

        #If word is guessed correctly
        if progress == guess_word:
            print(progress)
            print("You Win!!")
            break

        #Print the Progress
        print("Guess the word " + progress)

        #Get the Guess
        guess = input("Guess Character: ")

        #Check it is valid guess or not
        if guess in choices:
            letters_guessed += guess
        else:
            print("Enter Valid Character!!")
            guess = input("Guess Character: ")

        #Guessed Letter not in Word
        if guess not in guess_word:
            turns -= 1
            print("%s turns left!!" % turns)
            print(dict_turns[turns])
            if turns == 0:
                print("You Lose and Hangman Die")
                break
        
#Get the name of Player
name = input("Enter your name: ")

#Greet the Player
print("Welcome ",name)

#Seperate Greet and Game
print('-'*40)

#Show the number of letters in word and total attempts
print("Guess the word in less than 10 tries!!")

hangman_game()

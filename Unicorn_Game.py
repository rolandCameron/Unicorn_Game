#IMPORTS
import sys #Used to exit the program
import time #Used to make text more readable, and add dramatic effect
import random #Used to generate a random token

#VARIABLES
totalDeposited = 0
balance = 0

jackpotToken = open("jackpot.txt", "r")
neutralToken = open("neutral.txt", "r")
lossToken = open("loss.txt", "r")
logo = open("logo.txt", "r")

#CLASSES
class colours:
    RED = "\u001b[31m"
    YELLOW = "\u001b[33m"
    GREEN = "\u001b[32m"
    RESET = "\u001b[0m"

#FUNCTIONS
def Is_Int(string): #Checks if the argument is a string
    try:
        string = int(string)
        return True
    except:
        return False

def Initialise_Token(f, colour): #Remoces \n from the token files. Without this they are strangely spaced out. Also adds colouring to the tokens
    fLines = f.readlines() #Reads the text file
    fLines.insert(0, colour)
    for i in range(len(fLines)-1): #Runs for each line in the text file
        fLines[i+1] = fLines[i+1].strip("\n") #Removes '\n' from that line of the text
    f.close() #Closes the file
    fLines.append(colours.RESET)
    return fLines #Returns the list

def Show_Token(list): #Prints the token inputted
    for i in range(len(list)): #Runs for each line in the token
        print(list[i]) #Prints the line

def Cycle_Tokens(): #Cycles through the tokens like a slot machine
    for i in range(10): #Cycles 10 times
        print("\n" * 100) #'clears' screen
        token = random.randint(1, 4) #Chooses a random token
        if token == 1:
            Show_Token(jackpotToken) #Prints the jackpot token
        elif token == 4:
            Show_Token(lossToken) #Prints the loss token
        else:
            Show_Token(neutralToken) #Prints the neutral
        time.sleep((i+1)/10) #Waits more time in the earky iteratons, to simulate a slowing slot machine
    print("\n" * 100) #'clears' screen

#MAIN

##TEXT STRIPPING##
lossToken = Initialise_Token(lossToken, colours.RED) #Removes '\n' from the file and sets its colour
neutralToken = Initialise_Token(neutralToken, colours.YELLOW) #Removes '\n' from the file and sets its colour
jackpotToken = Initialise_Token(jackpotToken, colours.GREEN) #Removes '\n' from the file and sets its colour
logo = Initialise_Token(logo, colours.GREEN) #Removes '\n' from the file and sets its colour

Show_Token(logo) #Shows the logo when the program starts
print("\n\n\n") #Clears some lines to emphasise the logo

while True: #Starts main game loop
    if totalDeposited < 10: #Ensures the player never deposits more than $10
        gettingDeposit = True #Starts the gettingDeposit loop if the player hasn't deposited $10
    else:
        gettingDeposit = False #Ends the gettingDeposit loop if the player has deposited $10

    while gettingDeposit: #Gets the users deposit and error proofs it
        print("Your current balance is ${}.".format(balance)) #Tells the player their balance
        if input("Would you like to add more money to your account? (y/n) ").lower() == "y":#Asks the player if they want to make a deposit
            while gettingDeposit: #Starts a second loop if the player wants to make a deposit
                deposit = input("How much would you like to deposit? (Enter a whole $ value) ") #Gets the players deposit
                if Is_Int(deposit): #Checks if the deposit is an integer
                    deposit = int(deposit) #Turns the deposit into an int from a string
                    if deposit >= 1: #Checks that the user is inputting atleast 1
                        if not totalDeposited + deposit > 10: #Checks if the player's deposit will make their total deposited greater than $10
                            balance += deposit #Adds the player's deposit to their balance
                            totalDeposited += deposit #Increments the totalDeposited by the player's deposit

                            print("Deposit made, your balance is now ${}.".format(balance)) #Tells the player their new balance

                            gettingDeposit = False #Ends the gettingDeposit loop
                        else: #Runs if the player's deposit will exceed the maximum total deposit
                            print("Depositing that much money would result in you exceeding out $10 limit on spending. Please deposit less money.")
                    else: #Runs if the player inputs a number of 0 or lower
                        print("Please deposit at least $1.")
                else: #Runs if the player hasn't entered an integer
                    print("Make sure you are entering a whole dollar value, no decimal places, and that there are only numbers. ")
                    continue
        else: #Runs if the player doesn't want to make a deposit
            if balance < 1: #Checks if the player has enough money to play another round
                print("If you continue you wont have enough money to continue playing.")
                if input("Do you want to return to the investment options? (y/n) ").lower() == "y": #Double checks if the player wants to make a deposit
                    continue #Restarts the gettingDeposit loop
                else: #Runs if the player doesn't want to make a deposit
                    gettingDeposit = False #Ends the gettingDeposit loop
                    continue
            else: #Runs if the player has enough money to play another round
                gettingDeposit = False #Ends the gettingDeposit loop
                continue

    if balance >= 1: #Checks if the player has enough money to play another round
        gettingBet = True #Starts the gettingBet loop
    else: #Runs if the player doesn't have enough money to play another round
        print("You don't have a high enough balance to play another round, your final balance was ${}".format(balance)) #Tells the player their final balance
        print("Shutting down...")
        time.sleep(1)
        sys.exit() #Ends the program

    while gettingBet: #Gets the player's bet for this round, also does error proofing
        bet = input("How much would you like to bet on this round? (Must be more than $1 and a whole $ value) ") #Asks the player how much they would like to bet
        if Is_Int(bet):#Checks the players bet is an integer
            bet = int(bet) #Changes the players bet from a string to an integer
            if bet >= 1: #Checks if the bet is more than $1
                if not bet > balance: #Checks that the player hsa enough money to make this bet
                    print("You have bet ${}, this means a jackpot will be worth ${}!".format(bet, bet*5)) #Tells the player how much they have bet
                    gettingBet = False #Ends the gettingBet loop
                    balance -= bet #Subtracts the player bet from their balance
                    continue #Exits the gettingBet loop
                else: #Runs if the player tries to bet more money than they have
                    print("You can't bet more money than you have, you currently have ${}.".format(balance)) #Tells the player their balance
                    continue #Restarts this loop
            else: #Runs if the player tries to bet less than $1
                print("Please bet more than $1.")
                continue #Restarts this loop
        else: #Runs if the player doesn't enter an integer
            print("Make sure you are entering a whole dollar value, no decimal places, and that there are only numbers. ")
            continue #restarts this loop

    ##TOKEN RANDOMISER##
    #Runs the slot machine and produces a random token
    time.sleep(1) #Waits so the player can read text above
    token = random.randint(1, 4) #Selects a random token
    Cycle_Tokens() #Runs the slot machine of tokens
    if token == 1: #Runs if the jackpot token was selected
        Show_Token(jackpotToken) #Prints the jackpot token
        result = "win"
    elif token == 4: #Runs if the losing token was selected
        Show_Token(lossToken) #Prints the losing token
        result = "loss"
    else: #Runs if the neutral token was selected
        Show_Token(neutralToken) #Prints the neutral token
        result = "neutral"

    ##PAYOUT##
    #Provides the player with a pay out according to the token they recieved
    if result == "win": #Runs if the player won
        balance += bet*5 #Adds the players winnings to their balance
        print(colours.GREEN + "JACKPOT!") #Prints the text in green
        print("You won ${}!".format(bet*5))#Tells the player how much they won, still in green
        print("Your balance is now ${}".format(balance) + colours.RESET) #Tells the player their balance after the winnings have been added, resets text colour
    elif result == "loss": #Runs if the player lost
        print(colours.RED + "You lost :(") #Prints the text in red
        print("You won $0, and lost ${}.".format(bet)) #Tells the player how much money they lost, still in red
        print("Your balance is now ${}.".format(balance) + colours.RESET) #Resets the text colour and tells the player their balance
    elif result == "neutral": #Runs if the player got a neutral result
        balance += bet*0.5
        print(colours.YELLOW + "You got the neutral token.") #Prints the text in yellow
        print("Your balance is now ${}.".format(balance) + colours.RESET) #Tells the player their balance and resets the text colour

    playAgain = True
    while playAgain: #Asks whether the player wants to play another round or not
        if input("Would you like to play another round? (y/n) ").lower() == "y": #Asks if the player wants to play another round
            print("restarting... \n\n\n")  #Lets the player know their input was recognised
            time.sleep(0.5)
            playAgain = False #Ends the playAgain loop
            continue
        else: #Runs if the player doesn't want to play again
            print("Your current balance is ${}.".format(balance)) #Tells the player their balance
            if input("Are you sure you want to quit? (y/n) ").lower() == "n": #Makes sure the player wants to quit
                print("restarting... \n\n\n") #Lets the player know that their input was accepted
                time.sleep(0.5)
                playAgain = False #Ends the playAgain loop
                continue
            else: #Runs if the player doesn't want to play another game
                print("Your balance is ${}. Please ask to be paid this amount.".format(balance)) #Tells the player to ask for their alloted payment
                print("Shutting down...")
                time.sleep(1)
                sys.exit() #Exits the program






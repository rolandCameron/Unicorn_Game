#IMPORTS
import sys #Used to exit the program
import time #Used to make text more readable, and add dramatic effect

#VARIABLES
totalDeposited = 0
balance = 0

#FUNCTIONS
def Is_Int(string):
    try:
        string = int(string)
        return True
    except:
        return False

#MAIN

while True:
    if totalDeposited < 10:
        gettingDeposit = True
    else:
        gettingDeposit = False

    while gettingDeposit:
        print("Your current balance is ${}.".format(balance))
        if input("Would you like to add more money to your account? (y/n) ").lower() == "y":
            while gettingDeposit:
                deposit = input("How much would you like to deposit? (Enter a whole $ value) ")
                if Is_Int(deposit):
                    deposit = int(deposit)
                    if not totalDeposited + deposit > 10:
                        balance += deposit
                        totalDeposited += deposit

                        print("Deposit made, your balance is now ${}.".format(balance))

                        gettingDeposit = False
                    else:
                        print("Depositing that much money would result in you exceeding out $10 limit on spending. Please deposit less money.")

                else:
                    print("Make sure you are entering a whole dollar value, no decimal places, and that there are only numbers. ")
                    continue
        else:
            if balance < 1:
                print("If you continue you wont have enough money to continue playing.")
                if input("Do you want to add more money to your account? (y/n) ").lower() == "y":
                    continue
                else:
                    gettingDeposit = False
                    continue
            else:
                gettingDeposit = False
                continue

    if balance >= 1:
        gettingBet = True
    else:
        print("You don't have a high enough balance to play another round, your final balance was ${}".format(balance))
        print("Shutting down...")
        time.sleep(1)
        sys.exit()
    while gettingBet:
        bet = input("How much would you like to bet on this round? (Must be more than $1 and a whole $ value) ")
        if Is_Int(bet):
            bet = int(bet)
            if bet >= 1:
                if not bet > balance:
                    print("You have bet ${}, this means a jackpot will be worth ${}!".format(bet, bet*5))
                    gettingBet = False
                    balance -= bet
                    continue
                else:
                    print("You can't bet more money than you have, you currently have ${}.".format(balance))
                    continue
            else:
                print("Please bet more than $1.")
                continue
        else:
            print("Make sure you are entering a whole dollar value, no decimal places, and that there are only numbers. ")
            continue



'''
3. Generate a random token

4. Depending on the token, change their balance appropriately.
a. If jackpot(Unicorn) and 5 times how much they paid for the round
b. If neutral(Horse or zebra) add half as much as they paid for the round
c. If a loss(Donkey) pay nothing to the player

5. Show the user how much they earned

6. Ask if they want to play again
'''




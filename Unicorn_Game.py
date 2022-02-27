#IMPORTS

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
        if input("Would you like to add more money to your account? (y/n) ".lower()) == "y":
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
            gettingDeposit = False
            continue

'''
2. Ask how much the user wants to pay for this round(p), min of $1

3. Generate a random token

4. Depending on the token, change their balance appropriately.
a. If jackpot(Unicorn) and 5 times how much they paid for the round
b. If neutral(Horse or zebra) add half as much as they paid for the round
c. If a loss(Donkey) pay nothing to the player

5. Show the user how much they earned

6. Ask if they want to play again
'''




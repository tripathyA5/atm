class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def checkBalance(self):
        Balances = 1000
        print("Balances: " + str (Balances))
    def withDrawl(self, ammount):
        newAmmount = 1000-ammount
        print('You have withdrawn'+ str (ammount))
        print('Your remaining balance is'+ str(newAmmount))
def main():
    cardNumber = input("Enter your card number: ")
    pin = input("Enter your pin: ")
    user1 = Atm(cardNumber, pin)
    print("Choose your activity ")
    print("1.Balance Enquriy 2.withdrawl")
    activity = int(input("enter activity number :- ")) 
    if (activity == 1): 
        user1.checkBalance() 
    elif (activity == 2):
        ammount = int(input("enter the amount:- ")) 
        user1.withDrawl(ammount) 
    else: 
        print("enter a valid number")
main()

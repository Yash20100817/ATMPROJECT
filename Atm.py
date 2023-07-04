class atm:
    def __init__(self, cardNo, pin):
        self.cardNo=cardNo
        self.pin=pin
    def Check_Balance(self):
        print("Your balance is 10000 Rs.")
    def Withdrawal(self, amount):
        newAmount=1000-amount
        print("You have done withdrawal amount:  " +str(amount)+"Your remaining balance is: " +str(newAmount))
def main():
    cardNo=input("Insert your card no. ")
    pin=input("Enter your card pin. ")
    newUser=atm(cardNo, pin)
    print("Choose your activity ")
    print("1.Balance Enquiry   2.Withdrawal ")
    activity=int(input("Enter activity no. -"))
    if (activity==1):
        newUser.Check_Balance()
    elif (activity==2):
        amount=int(input("Enter the amount of money you will like to withdraw "))
        newUser.Withdrawal(amount)
    else:
        print("Enter a valid number!! ")
if __name__ == "__main__":
    main()
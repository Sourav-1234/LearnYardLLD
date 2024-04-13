class BankAccount:
    def __init__(self):
        self.balance=0
        self.transactions=[]
    
    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f"Deposited :{amount}")

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            self.transactions.append(f"Withdrawn:{amount}")
    

    def generate_statement(self):
        print("Bank Statement")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance:{self.balance}")


if __name__ == "__main__":
    account=BankAccount()
    account.deposit(500)
    account.withdraw(100)
    account.generate_statement()

#Now this code is violating the Single Responsibilty Principle where we can write the generate bank statement in the different class 
#To segregate it the class are seggregated





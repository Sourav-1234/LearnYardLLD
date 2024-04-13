#Bank Account is  only responsible about maintaining the account balance 

class BankAccount:
    def __init__(self):
        self.balance=0
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient Balance")
            return 
        else:
            self.balance-=amount
    


#Transaction is only responsible for  keeping the records intact in the class


class Transaction:
    def __init__(self):
        self.transactions=[]

    def record_deposit(self,amount):
        self.transactions.append(f"Deposited :{amount}")
    
    def record_withdraw(self,amount):
        self.transactions.append(f"Withdraw :{amount}")
    
    def generate_statement(self):
        print("Bank Statement")
        for transaction in self.transactions:
            print(transaction)


if __name__ == "__main__":
    account=BankAccount()
    transaction_manager=Transaction()

    account.deposit(400)
    transaction_manager.record_deposit(400)
    account.withdraw(100)
    transaction_manager.record_withdraw(100)
    transaction_manager.generate_statement()



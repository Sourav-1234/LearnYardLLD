#BanK Account is Open for Inheritance for extension but closed for modification

# Now to add new feature related to the interest rate we are adding the feature directly into the BankAccount 
# Class but it is violating the Open Close Principle since we are modifying the class


class BankAccount:
    def __init__(self,interest_rate):
        self.balance=0
        self.interest_rate=interest_rate
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient Balance")
            return 
        else:
            self.balance-=amount
    def apply_interest(self):
        self.balance+=self.balance*self.interest_rate
    
#Savings Account now adds new functionality to its class without modifying the BankAccount Class


# class SavingsAccount(BankAccount):
#     def __init__(self,interest_rate):
#         super().__init__()
#         self.interest_rate = interest_rate
    
#     def apply_interest(self):
#         self.balance+=self.balance*self.interest_rate


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
    account=BankAccount(0.02)
    transaction_manager=Transaction()

    account.deposit(400)
    transaction_manager.record_deposit(400)
    account.withdraw(100)
    transaction_manager.record_withdraw(100)
    account.apply_interest()
    transaction_manager.generate_statement()
    print(f"Current Balance:{account.balance}")



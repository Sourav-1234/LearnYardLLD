#Now instead of Bank Account dependent on concrete class it is dependent on the abstract class thus
#the dependency inversion principle is being demonstrated
from abc import ABC,abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def apply_interest(self):
        pass


class BankAccount(Account):
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
    

    def apply_bank_fee(self,fee):
        if fee>self.balance:
            print(f"Insufficient funds to cover the fees")
        
        else:
            self.balance=self.balance-fee
    
    def apply_interest(self):
        pass

#Savings Account now adds new functionality to its class without modifying the BankAccount Class


class SavingsAccount(BankAccount):
    def __init__(self,interest_rate):
        super().__init__()
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance+=self.balance*self.interest_rate


#Transaction is only responsible for  keeping the records intact in the class


class Transaction:
    def __init__(self):
        self.transactions=[]

    def record_deposit(self,amount):
        self.transactions.append(f"Deposited :{amount}")
    
    def record_withdraw(self,amount):
        self.transactions.append(f"Withdraw :{amount}")
    
    def record_bank_fee(self,amount):
        self.transactions.append(f"Bank Fee:{amount}")
    
    def generate_statement(self):
        print("Bank Statement")
        for transaction in self.transactions:
            print(transaction)

#Liskov Substitution Principle jhas been implemented if now Current Accounbt is added we need not have to change anything 


class Operations:
    def __init__(self,account,transaction_manager):
        self.account = account
        self.transaction_manager = transaction_manager

    def perform_operations(self,deposit_amount,withdrawn_amount,bank_fee):
        self.account.deposit(deposit_amount)
        self.transaction_manager.record_deposit(deposit_amount)
        self.account.withdraw(withdrawn_amount)
        self.transaction_manager.record_withdraw(withdrawn_amount)
        self.account.apply_bank_fee(bank_fee)
        self.transaction_manager.record_bank_fee(bank_fee)
        self.account.apply_interest()
        self.transaction_manager.generate_statement()

        print(f"Current Balance:{self.account.balance}")



if __name__ == "__main__":
    account=BankAccount()
    saving_account=SavingsAccount(0.02)
    transaction_manager=Transaction()

    operation=Operations(account,transaction_manager)
    operation.perform_operations(500,100,10)

    operation1=Operations(saving_account,transaction_manager)
    operation1.perform_operations(600,200,50)




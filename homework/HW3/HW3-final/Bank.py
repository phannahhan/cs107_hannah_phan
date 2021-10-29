#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


# In[2]:


AccountType.SAVINGS
AccountType.SAVINGS == AccountType.SAVINGS
AccountType.SAVINGS.name


# In[3]:


class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
        
    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
        elif amount < 0:
            raise ValueError('You are not able to withdraw a negative amount')
        elif amount > self.balance:
            raise ValueError('You are not able to withdraw an amount greater than your balance')   
        
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError('You are not able to deposit a negative amount') 
        
    def __str__(self):
        return f"Owner: {self.owner}; Account type: {self.accountType}."
    
    def __len__(self):
        return f"Balance: {self.balance}."


# In[5]:


class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}
        
    def addAccount(self, accountType):
        
        account = BankAccount(self.owner, accountType)
        
        if accountType in self.accounts:
            raise ValueError(f'{accountType.name} account already exists.')
        elif accountType.name == 'SAVINGS':
            self.accounts[accountType] = account
        elif accountType.name == 'CHECKING':
            self.accounts[accountType] = account
        else:
            raise NameError('Not an account type.')
              
        
    def getBalance(self, accountType):
        if accountType in self.accounts:
            account = self.accounts[accountType]
        else:
            raise NameError("You do not have an account of this type to get a balance from")
        return account.balance
    
    
        
    def deposit(self, accountType, amount):
        
        if accountType in self.accounts:
            if accountType.name == 'SAVINGS':
                account = self.accounts[accountType]
                account.deposit(amount)
            elif accountType.name == 'CHECKING':
                account = self.accounts[accountType]
                account.deposit(amount)
        else:
            raise NameError("You do not have an account of this type to deposit in.")

    def withdraw(self, accountType, amount):
        
        if accountType in self.accounts:
            account = self.accounts[accountType]
            if accountType.name == 'SAVINGS':
                account = self.accounts[accountType]
                account.withdraw(amount)
            elif accountType.name == 'CHECKING':
                account = self.accounts[accountType]
                account.withdraw(amount)
        elif accountType not in self.accounts and accountType in list(AccountType):
            raise NameError("You do not have an account of this type to withdraw from. Make sure to create either a 'SAVINGS' or 'CHECKING' account first")
        # double check case for non-existent account type
        elif accountType.name not in list(AccountType):
            raise NameError("This is not a type of account")
        
    def __str__(self):
        return f"Owner: {self.owner}; Accounts: {self.accounts.keys()}."


# In[6]:


# In[ ]:


def ATMSession(bankUser):
    def Interface():
        while True:
            ui1 = input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n")
            try:
                assert ui1 in ['1','2','3','4','5'], f'Invalid input; returning to main menu'
                ui1 = int(ui1)
            except Exception as e:
                print(e)
                print("Invalid; Returning to main menu")    
            
            if ui1 == 1:
                print("Exiting")
                break

            elif ui1 in ['2', '3', '4', '5']:

                try:
                    ui2 = input("Enter Option:\n1)Checking\n2)Savings\n")
                    assert ui2 in [1,2], f'Invalid input; returning to main menu'
                    ui2 = int(ui2) 
                    if ui2 == 1:
                        accountType = AccountType.CHECKING

                    elif ui2 == 2:
                        accountType = AccountType.SAVINGS

                    elif ui1 == 2:
                        bankUser.addAccount(accountType)

                    elif ui1 == 3:
                        print(bankUser.getBalance(accountType))

                    elif ui1 == 4 or ui1 == 5:
                        ui3 = int(input("Enter Non-Negative Integer Amount:\n"))

                        if ui1 == 4:
                            bankUser.deposit(accountType, ui3)

                        elif ui1 == 5:
                            bankUser.withdraw(accountType, ui3)
                    # else:
                    #     raise ValueError("Invalid input")
                except Exception as e:
                    print(e)
                    print("Invalid; Returning to main menu")    
        else:
            print('Not an option; returning to main menu.')
    return Interface
            

def main():
    bankUser = BankUser('Dummy')
    session = ATMSession(bankUser)
    session()
    
if __name__ == '__main__':
    main()
 


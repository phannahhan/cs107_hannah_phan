#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Bank as bank
from Bank import BankAccount
from Bank import BankUser
from Bank import AccountType
from enum import Enum
import sys


# In[12]:


def test_over_addAccount(): 
    user = BankUser("Joe already has CHECKING");
    user.addAccount(AccountType.CHECKING);
    user2 = BankUser("Joe already has SAVINGS");
    user2.addAccount(AccountType.SAVINGS);
    
    try:
        user.addAccount(AccountType.CHECKING); # can't have more than 1 CHECKING account
    except Exception as e:
        print(e); #print the message for the Exception
        
    try:
        user2.addAccount(AccountType.SAVINGS); # can't have more than 1 SAVINGS account
    except Exception as e:
        print(e); #print the message for the Exception

def test_over_withdraw():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    user2 = BankUser("Joe no Checking");
    user2.addAccount(AccountType.SAVINGS)
    user3 = BankUser("Joe no Savings");
    user3.addAccount(AccountType.CHECKING);
    
    try:
        user.withdraw(AccountType.SAVINGS, 1000); # can't withdraw more than the balance
    except Exception as e:
        print(e); #print the message for the Exeption
        
    try:
        user.withdraw(AccountType.SAVINGS, -1); # can't withdraw a negative value
    except Exception as e:
        print(e); #print the message for the Exeption
        
    try:
        user2.withdraw(AccountType.SAVINGS, 10); # Withdrawing from a CHECKING account when user only has SAVINGS
    except Exception as e:
        print(e);
        
    try:
        user3.withdraw(AccountType.CHECKING, 10); # Withdrawing from a SAVINGS ccount when user only has CHECKING
    except Exception as e:
        print(e);
    
def test_over_deposit(): 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.addAccount(AccountType.CHECKING);
    user.deposit(AccountType.SAVINGS, 10);
    user2 = BankUser("Joe no Checking");
    user2.addAccount(AccountType.SAVINGS)
    user3 = BankUser("Joe no Savings");
    user3.addAccount(AccountType.CHECKING)
    
    try:
        user.deposit(AccountType.SAVINGS, -1); # should not be able to deposit negative amounts in SAVINGS
    except Exception as e:
        print(e);
        
    try:
        user.deposit(AccountType.CHECKING, -1); # should not be able to deposit negative amounts in CHECKING
    except Exception as e:
        print(e);
        
    try:
        user2.deposit(AccountType.CHECKING, 10); # should not be able to deposit into non-existent account
    except Exception as e:
        print(e);
        
    try:
        user3.deposit(AccountType.SAVINGS, 10); # should not be able to deposit into non-existent account
    except Exception as e:
        print(e);
        
def test_over_getBalance():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.addAccount(AccountType.CHECKING);
    user.deposit(AccountType.SAVINGS, 10);
    user.deposit(AccountType.CHECKING, 10);
    user2 = BankUser("Joe no Checking");
    user3 = BankUser("Joe no Savings");
    
    try:
        user2.getBalance(AccountType.CHECKING) # can't get CHECKING balance if you don't have CHECKING
    except Exception as e:
        print(e);
        
    try:
        user3.getBalance(AccountType.SAVINGS) # can't get SAVINGS balance if you don't have SAVINGS
    except Exception as e:
        print(e);
        
test_over_addAccount();
test_over_withdrawal();
test_over_deposit();
test_over_getBalance();


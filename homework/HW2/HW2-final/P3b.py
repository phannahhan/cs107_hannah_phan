#!/usr/bin/env python
# coding: utf-8

# In[10]:


def make_withdrawal(balance):
    def final_balance(withdrawal_amount):
        # if withdrawal amount is greater than balance return None
        if withdrawal_amount > balance:
            return None
        else:
        # otherwise, return balance - withdrawal amount
            new_bal = balance - withdrawal_amount
            balance = new_bal
            return new_bal
    return final_balance


# In[12]:


wd = make_withdrawal(300)


# In[13]:


wd(50)


# In[14]:


wd(100)


# In[19]:


print('The balance is not updated because reassigning the variable "balance" occurs locally within the inner function block, so the scope is contained within the inner function and any blocks within it. Thus, when we reference balance in the demo, the Python interpreter at module load time decides that the global scope of the balance variable should not be used inside the local scope of the inner final_balance function. Since the default behavior for binding is to search the local namespace first, we get the problem of referencing a local variable before it is assigned locally.')


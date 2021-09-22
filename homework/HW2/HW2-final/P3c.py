#!/usr/bin/env python
# coding: utf-8

# In[4]:


def make_withdrawal(balance):
    def final_balance(withdrawal_amount):
        # Declare balance as a nonlocal variable using the nonlocal keyword.
        nonlocal balance
        if withdrawal_amount > balance:
            return None
        else:
            new_bal = balance - withdrawal_amount
            balance = new_bal
            return new_bal
    return final_balance


# In[5]:


wd = make_withdrawal(300)


# In[6]:


wd(50)


# In[7]:


wd(100)


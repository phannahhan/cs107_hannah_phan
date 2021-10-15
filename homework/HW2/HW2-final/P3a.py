#!/usr/bin/env python
# coding: utf-8

# In[56]:


def make_withdrawal(balance):
    def final_balance(withdrawal_amount):
        if withdrawal_amount > balance:
            return None
        else:
            new_bal = balance - withdrawal_amount
            return new_bal
    return final_balance


# In[57]:


wd = make_withdrawal(300)


# In[58]:


wd(50)


# In[59]:


wd(100)


# In[60]:


print('Consecutive withdrawals do not behave as expected because the original balance does not change after each withdrawal. This is because we are not reassigning the balance variable to the final balance after the withdrawal.')


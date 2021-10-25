#!/usr/bin/env python
# coding: utf-8

# In[20]:


import sympy
from sympy import diff, exp
from sympy import *
from sympy.abc import x,y
init_printing(use_unicode=True)


# In[24]:


expr = x - exp(-2*(sin(4*x)**2))

print(diff(expr, x))


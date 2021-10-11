#!/usr/bin/env python
# coding: utf-8

# In[19]:


# from Regression import Regression
# import Regression as Rg 
import numpy as np
import Regression as Rg

from sklearn import datasets
from sklearn.model_selection import train_test_split


# In[20]:


linear_rg = Rg.LinearRegression()
ridge_rg = Rg.RidgeRegression()


# In[31]:


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alpha = 0.1
models = [linear_rg, ridge_rg]
# use sklearn to compare coeffs and intercept because according to the tf r_squared isn't as good
# ridge regression will have a larger r squared value on the test set so ridge regression will work better

for model in models:
    model.set_params(alpha=0.1)
    model.fit(X_train, y_train);
    model.score(X_test, y_test)
    print(f"{model} Score: {model.score(X_test, y_test)}")
print(ridge_rg.get_params())


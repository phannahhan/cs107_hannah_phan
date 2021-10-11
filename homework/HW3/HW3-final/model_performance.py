#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import Regression as Rg
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split


# In[2]:


linear_rg = Rg.LinearRegression()
ridge_rg = Rg.RidgeRegression()


# In[49]:


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alphas = np.arange(0.1, 10.1, 1).tolist()

# Linear Regression 
linear_scores = []
for i in range(len(alphas)):
    linear_rg.fit(X_train, y_train)
    linear_scores.append(linear_rg.score(X_test, y_test))
    
# Ridge Regression
ridge_scores = []
for i in range(len(alphas)):
    ridge_rg.set_params(alpha = alphas[i])
    ridge_rg.fit(X_train, y_train)
    ridge_scores.append(ridge_rg.score(X_test, y_test))

plt.plot(alphas, linear_scores, label='Linear Model')
plt.plot(alphas, ridge_scores, label='Ridge Model')
    
plt.legend()

plt.xlabel("Alpha")
plt.ylabel("R-Squared")
plt.ylim([0, 1])
plt.title('Model Performance for Linear vs Ridge Model for Different Alphas')
plt.show(block = True)


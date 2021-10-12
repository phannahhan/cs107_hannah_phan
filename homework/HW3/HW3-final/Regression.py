#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.linalg import inv, pinv


# In[2]:


class Regression():

    def __init__(self):
        self.params = { }

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        # can set this in Ridge subclass
        # loop through keyword args and set them as key-value pairs in a dictionary
        # double check how to loop
        #for key in kwargs:
        #    self.params['alpha'] = kwargs['alpha']
            
        for key, val in kwargs.items():
            if key in ('slope', 'intercepts'):
                self.params[key] = val
            elif key == 'alpha':
                self.alpha = val
                # self.params['alpha'] = self.alpha
            else:
                raise TypeError("invalid argument '%s'" % key)

    def fit(self, X, y):
        raise NotImplementedError
        
    def predict(self, X):
        # X has a shape (10,) here
        return X@self.params['best_fit_coeff'] + self.params['intercept']

    def score(self, X, y):
        sst = 0
        sse = 0
        for i in range(len(y)):
            sst = sst + ((y[i] - np.mean(y)) ** 2)
            sse = sse + ((y[i] - self.predict(X[i])) ** 2)
        r_squared = 1 - (sse/sst)
        return r_squared


# In[3]:


class LinearRegression(Regression):
    
    def __init__(self):
       super(LinearRegression, self).__init__()
        
    def fit(self, X, y):
        # append a column of 1's with the same # of rows as X to X to create the intercept, pass as a tuple
        new_column = np.ones((X.shape[0], 1))
        
        # append column to front of X, X now will have shape (353,11)
        X = np.append(new_column, X, axis = 1)
        
        # need to create dictionary here because we don't have data to make it in the constructor
        # best_fit_coeff is a vector with 11 rows (11,)
        best_fit_coeff = (pinv(X.transpose()@X)@X.transpose())@y
        
        # params = {"best_fit_coeff": best_fit_coeff, "intercept": X[0]}
        params = {"best_fit_coeff": best_fit_coeff[1:], "intercept": best_fit_coeff[0]}
        self.params = params


# In[4]:


class RidgeRegression(LinearRegression):
    # alpha = 0.1 is a default value so that you can define a ridgeregression obj without passing alpha
    def __init__(self, alpha = 0.1):
        super(RidgeRegression, self).__init__()
        #self.alpha = alpha
    
    def set_params(self, **kwargs):
        for key, val in kwargs.items():
            if key in ('slope', 'intercepts'):
                self.params[key] = val
            elif key == 'alpha':
                self.alpha = val
                self.alpha = kwargs['alpha']
            else:
                raise TypeError("invalid argument '%s'" % key)
        
    def fit(self, X, y):
        # append a column of 1's with the same # of rows as X to X to create the intercept
        Xmean = np.mean(X, axis=0)
        scale = 1 / np.sqrt(np.sum((X - Xmean)**2, axis=0))
        Xs = X * scale
        
        new_column = np.ones((Xs.shape[0], 1))
        Xs = np.append(new_column, Xs, axis = 1)
        
        # how to pull alpha to make gamma? Can we get it from set_params? Yes
        # what shape should gamma have? X^T*X will be pxp, so gamma will be pxp
        gamma = self.alpha*np.identity(np.shape(Xs)[1]) 
        gamma[0, 0] = 0
        
        best_fit_coeff = (pinv(Xs.transpose()@Xs + gamma.transpose()@gamma))@Xs.transpose()@y
        params = {"best_fit_coeff": best_fit_coeff[1:]*scale, "intercept": best_fit_coeff[0]}
        self.params = params
        


# In[ ]:





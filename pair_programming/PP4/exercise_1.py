#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[36]:


def layer(shape, actv):
    def layer_output(inputs, weights, bias):
        return actv(np.dot(inputs, weights) + bias)
    return layer_output


# t: shape (1,100)
# w: shape (100, x)
# np.dot(t,w): shape = (1,x)
# b: shape = (1,x)
# formula: np.dot(t,w) + b
# h2: shape = (1,1)


# In[40]:


# shape 100 by 1
t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

shape1 = [np.size(t), np.size(t)] 
shape2 = [np.size(t), np.size(t)]

# create matrix 100 rows by 3 cols
w1 = np.random.uniform(0.0, 1.0, size = (100, 3))
w2 = np.random.uniform(0.0, 1.0, size = (3, 1))

# bias shape 1 by 3
b1 = np.random.uniform(0.0, 1.0, size = (1, 3))
b2 = np.random.uniform(0.0, 1.0, size = (1, 1))

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer


# In[ ]:


h1.shape


# In[39]:


h2.shape


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Partner: Xinyi Li


# In[5]:


import numpy as np


# In[6]:


class Layer():
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weight = np.random.rand(*self.shape) # input to np.random.rand is 2 args
        self.bias = np.random.rand(1, self.shape[1])
        
    def forward(self, inputs):
        # introduces nonlinearity 
        return self.actv(inputs@self.weight+np.repeat(self.bias, inputs.shape[0], axis=0))
    def __call__(self, inputs):
        return self.forward(inputs)
    def __str__(self):
        return f"shape: {self.shape}, activation function: {self.actv}"
    def __repr__(self):
        return f"shape: {self.shape}, activation function: {self.actv}, weight: {self.weight}, bias: {self.bias}"


# In[7]:


n = 100
# the first slot should be the number of inputs to the layers and the second slot should be the number of nodes in the layer
shape1 = (20,10)
shape2 = (shape1[1], 1)
inputs = np.random.rand(n, shape1[0])
actv = np.tanh

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1(inputs)
h2 = layer2(h1)
print(layer1)
print(layer2.__repr__())


# In[ ]:





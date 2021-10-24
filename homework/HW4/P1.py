#!/usr/bin/env python
# coding: utf-8

import numpy as np

import sympy
from sympy import diff, exp
from sympy import *
from sympy.abc import x,y
init_printing(use_unicode=True)

import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


def numerical_diff(f,x, h = 0.01):
    # compute forward difference
    # f : vectorized function of one variable x
    # x : compute derivative at x
    # method: string 'forward' for forward method f(x+h) - f(x))/h
    return (f(x + h) - f(x))/h

x_vals = np.arange(0.2, 0.4, 0.01)
h_vals = [1e-1, 1e-7, 1e-15]

# compute numerical differentiation
# how to iterate with xval and hval at the same time?
num_diff = []
for h_val in h_vals:
    # make empty lists for each h_val
    h_list = []
    for x_val in x_vals:
        # append to the h list
        h_list.append(numerical_diff(np.log, x_val, h_val))
    # append to num_diff list, 3 elements, each element is an h_list
    num_diff.append(h_list)


# compute the exact derivative
# derivative of lnx is 1/x
exact_deriv = []
for x_val in x_vals:
    exact_deriv.append(1/x_val)

# plot numerical differentiation vs. exact differentiation
plt.figure(figsize=(12,5))
plt.plot(x_vals, num_diff[0], 'r--', label = 'h = 1x1e-1')
plt.plot(x_vals, num_diff[1], 'b--', label = 'h = 1x1e-7')
plt.plot(x_vals, num_diff[2], 'g--', label = 'h = 1x1e-15')
plt.plot(x_vals, exact_deriv,'y*',label = 'Analytical Derivative')

plt.title('Numerical vs. Exact Differentiation of y = ln(x)')
plt.xlabel('x')
plt.ylabel('dydx')
plt.legend(loc='best')

print("Answer to Q-a: h = 1*1e-7 most closely approximates the true derivative. Even though smaller step sizes would reduce error, when h is too small as with h = 1*1e-15, there are python truncation errors since our computers can only keep track of a finite number of decimals, which results in this choppy line. When h is too large, the dydx values fall below the true derivative")
print("Answer to Q-b: Automatic differentiation does not introduce round-off errors because unlike numerical differentiation, it does not use finite differentiating, but rather chain-rule based techniques for analytical derivatives. AD also uses less computing power in the process. More specifically, automatic differentiation uses arithmetic operations, functions, and the chain rule to break down complex derivatives into simpler ones. Reducing a function to a composite of these primitives allows our computers to compute the derivatives and combine them to get the derivative of the entire function all while using the same number of arithmetic operations as the original function.")


plt.show(block = True)


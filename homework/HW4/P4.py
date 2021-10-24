#!/usr/bin/env python
# coding: utf-8

class AutoDiffToy:
    def __init__(self, val, der = 1.0):
        self.val = val
        self.der = der
        
    def __add__(self, other):
        try:
            new_val = self.val + other.val
            new_der = self.der + other.der
            return AutoDiffToy(new_val, new_der)
        except AttributeError:
            new_val = self.val + other
            new_der = self.der + 0
            return AutoDiffToy(new_val, new_der)
        
    def __radd__(self, other):
        try:
            new_val = other.val + self.val
            new_der = other.der + self.der
            return AutoDiffToy(new_val, new_der)
        except AttributeError:
            new_val = other + self.val
            new_der = 0 + self.der
            return AutoDiffToy(new_val, new_der)
        

    def __mul__(self, other):
        try:
            new_val = self.val * other.val
            new_der = self.der * other.val + other.der * self.val
            return AutoDiffToy(new_val, new_der)
        except AttributeError:
            new_val = self.val * other
            new_der = self.der * other
            return AutoDiffToy(new_val, new_der)
        
    def __rmul__(self, other):
        try:
            new_val = other.val * self.val
            new_der = other.val * self.der + self.val * other.der
            return AutoDiffToy(new_val, new_der)
        except AttributeError:
            new_val = other * self.val
            new_der = other * self.der
            return AutoDiffToy(new_val, new_der)
        


# demo

a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0

f1 = alpha * x + beta
print(f1.val, f1.der)

f2 = x * alpha + beta
print(f2.val, f2.der)

f3 = beta + alpha * x
print(f3.val, f3.der)

f4 = beta + x * alpha
print(f4.val, f4.der)


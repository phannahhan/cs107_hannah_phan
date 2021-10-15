import numpy as np
import matplotlib.pyplot as plt

def outer(r):
    def inner(x):
        return x**r, r*x**(r-1)
    return inner

def my_pow(x, r):
    return x**r, r*x**(r-1)

if __name__ == "__main__":
    print(my_pow(3, 2))
    a = outer(2)
    print(a(3))
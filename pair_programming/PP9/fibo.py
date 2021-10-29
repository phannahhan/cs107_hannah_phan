#!/usr/bin/env python
# coding: utf-8

# In[20]:


# groupmates: William, Arno, Jie, Hannah

class Fibonacci():
    def __init__(self, terms):
        self.counter = terms

    # tells the next function in the FibonacciIterator class how to iterate, so return the index of the last term
    def __iter__(self):
        # reset iter method
        # return an object that exposes an __next__ method.
        # self is a Fibonacci object
        return FibonacciIterator(self.counter)
    

#     def __next__(self):
        
#         #  Once we return the count of fibo numbers we need, stop the iteration

#         if self.counter == 0:
#            raise StopIteration

#         self.counter -= 1

#         nextFib       = self.curFib + self.nextFib
#         self.curFib   = self.nextFib
#         self.nextFib  = nextFib

#         return self.curFib

# define iterator class so that we can iterate over the class multiple times, create multiple iterable objects
class FibonacciIterator():
    def __init__(self, Fibonacci):
        self.counter = Fibonacci
        self.curFib  = 0
        self.nextFib = 1
        
    def __iter__(self):
        # return current state of where you're at
        return self
    
    def __next__(self):
        
        #  Once we return the count of fibo numbers we need, stop the iteration

        if self.counter == 0:
           raise StopIteration

        self.counter -= 1

        nextFib       = self.curFib + self.nextFib
        self.curFib   = self.nextFib
        self.nextFib  = nextFib

        return self.curFib
    

fib = Fibonacci(10)
fib2 = iter(fib)
print(next(fib2))
print(next(fib2))
print(next(fib2))
#print(fib2)
list(iter(fib))


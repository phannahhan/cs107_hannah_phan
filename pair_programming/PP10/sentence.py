#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Groupmmates: Arno Cai, Alex Ho, Hannah Phan

import 
# class SentenceIterator:
#     def __init__(self, words): 
#         self.words = words 
#         self.index = 0

#     def __next__(self): 
#         try:
#             word = self.words[self.index] 
#         except IndexError:
#             raise StopIteration() 
#         self.index += 1
#         return word 

#     def __iter__(self):
#         return self

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        #return SentenceIterator(self.words)
        for word in self.words:
            yield word # returns each word one at a time, yield already has the next function within it a generator
    

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    
if __name__ == '__main__':
    sentence1 = 'this is my test sentence'
    exampleclass = Sentence(sentence1)
    test = iter(exampleclass)
    print(next(test))
    print(next(test))


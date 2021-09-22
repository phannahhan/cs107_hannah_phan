#!/usr/bin/env python
# coding: utf-8

# In[96]:


def dna_complement(dna_sequence):
    # bases with upper and lower cases
    bases = ['A', 'a', 'T', 't', 'G', 'g', 'C', 'c']
    
    # setting complements for bases. lower case bases return upper case complements
    complement = {'A': 'T', 'a': 'T', 'T': 'A', 't': 'A', 'C': 'G', 'c': 'G', 'G': 'C', 'g': 'C'}
    
    if not dna_sequence:
        return None
    
    # return None if there is any element in dna string that is not in the bases list
    elif not any(base in dna_sequence for base in bases):
        return None
    
    # otherwise, join complement of each base in string dna_sequence (slice through by 1)
    else:
        return dna_sequence, ''.join([complement[base] for base in dna_sequence[::]]);
        


# In[97]:


dna_complement('AaTtGgCc')


# In[95]:


dna_complement('#ABCD!!')


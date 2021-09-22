#!/usr/bin/env python
# coding: utf-8

# In[93]:


def dna_complement(dna_sequence):
    bases = ['A', 'a', 'T', 't', 'G', 'g', 'C', 'c']
    complement = {'A': 'T', 'a': 'T', 'T': 'A', 't': 'A', 'C': 'G', 'c': 'G', 'G': 'C', 'g': 'C'}
    if not dna_sequence:
        return None
    elif not any(base in dna_sequence for base in bases):
        return None
    else:
        return dna_sequence, ''.join([complement[base] for base in dna_sequence[::1]]);
        


# In[94]:


dna_complement('AaTtGgCc')


# In[95]:


dna_complement('#ABCD!!')


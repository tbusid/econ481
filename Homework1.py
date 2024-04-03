#!/usr/bin/env python
# coding: utf-8

# ## Homework 1

# ## Exercise 0

# In[ ]:


def github() -> str:
    """
    Returns a link to my solutions on GitHub.
    """

    return "https://github.com/tbusid/econ481/blob/main/Homework1.py"


# ## Exercise 1

# In[1]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as plt
import seaborn as sb


# ## Exercise 2

# In[6]:


def evens_and_odds(n: int) -> dict:
    """
    Function that takes as argument a natural number n and returns a dictionary with two keys, “evens” and “odds”.
    "odds" returns the sum of odd natural numbers less than n. "evens" returns the sum of even natural numbers less
    than n.
    """
    i = 0
    evens = 0
    odds = 0
    for i in range(n):
        if i % 2 == 0:
            evens += i
        else: 
            odds += i
    return {'evens': evens, 'odds': odds}
evens_and_odds(4)


# ## Exercise 3

# In[39]:


from typing import Union

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    Function time_diff returns the differnce in time between two different dates.
    """
    dt1 = datetime.strptime(date_1, '%Y-%m-%d')
    dt2 = datetime.strptime(date_2, '%Y-%m-%d')
    dt3 = dt2-dt1
    if out == 'string':
        dt4 = str(abs(dt3.days))
        return 'There are ' + dt4 + ' days between the two dates.'
    else:
        return abs(dt3.days)
time_diff('2020-01-01', '2020-01-02', 'string')


# ## Exercise 4

# In[37]:


def reverse(in_list: list) -> list:
    """
    This function reverses the order of items in a list.
    """

    for i in range(len(in_list) // 2):
        in_list[i], in_list[-1-i] = in_list[-1-i], in_list[i]
    
    return in_list
reverse(['a', 'b', 'c'])


# ## Exercise 5

# In[1]:


def prob_k_heads(n: int, k: int) -> float:
    """
    Function that finds the probability of getting k heads from n flips of a coin.
    """
    fact = 1
    for i in range(1, n+1):
        fact *= i
    k = 3
    nminuskfac = 1
    for i in range(1, n-k+1):
        nminuskfac *= i
    nchoosek = 1
    for i in range(k+1, n+1):
        nchoosek *= i
    nchoosek /= nminuskfac
    prob = nchoosek / 2 ** n
    return prob
prob_k_heads(6,3)


# In[ ]:





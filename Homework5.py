#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 5

# ## Exercise 0

# In[1]:


def github() -> str:
    """
    This function returns a link to my solution on GitHub.
    """

    return "https://github.com/tbusid/econ481/edit/main/Homework5.py"


# ## Exercise 1

# In[24]:


import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import time
def scrape_code(url: str) -> str:
    """
    This function takes as its argument a lecture’s URL on the course website
    and returns a string containing all the python code in the lecture formatted 
    in such a way that we could save it as a python file and run it without syntax issues.
    """
    req_obj = requests.get(url)
    soup = BeautifulSoup(req_obj.text, 'html.parser')
    codes = [x.text for x in soup.find_all('code', class_ = 'sourceCode python')]
    df_list = []
    for code in codes:
        codelines = code.strip().split('\n')
        for codeline in codelines:
            if not codeline.startswith('%'):
                df_list.append(codeline)
    output = '\n'.join(df_list)
    return output

url = 'https://lukashager.netlify.app/econ-481/02_numerical_computing_in_python'
print(scrape_code(url))


# In[ ]:





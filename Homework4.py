#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 4

# ## Exercise 0

# In[23]:


def github() -> str:
    """
    This function returns a link to my solution on GitHub.
    """

    return "https://github.com/tbusid/econ481/edit/main/Homework4.py"


# ## Exercise 1

# In[24]:


import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Function that accesses the file on Tesla stock price history on
    the course website and returns that data as a data frame.
    """
    df = pd.read_csv('https://lukashager.netlify.app/econ-481/data/TSLA.csv', index_col=0, parse_dates=True)
    return df
print(load_data())


# ## Exercise 2

# In[25]:


import matplotlib.pyplot as plt
def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Function that takes our solution from exercise one and 2 string dates and
    plots the closing price of the stock between those dates as a line graph.
    """
    tes = df["Close"]
    fig, ax = plt.subplots()
    tes.plot(ax=ax, color="black")
    ax.set_xlim([start, end])
    ax.set_title("Tesla Closes from " + start + " to " + end)
plot_close(load_data(), '2010-06-29', '2024-04-15')


# ## Exercise 3

# In[27]:


import statsmodels.api as sm
def autoregress(df: pd.DataFrame) -> float:
    """
    Function that takes our solution from exercise one and returns the t statistic on beta from a regression.
    """
    df["dx"] = df["Close"].diff()
    df["dxs"] = df["dx"].shift(1)
    df.dropna(subset=["dx", "dxs"], inplace = True)
    dx = df["dx"]
    dxs = df["dxs"]
    model = sm.OLS(dx, dxs).fit(cov_type = "HC1")
    t = model.tvalues["dxs"]
    return t
print(autoregress(load_data()))


# ## Exercise 4

# In[28]:


def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Function that takes our solution from exercise one and returns the t statistic on beta 
    from a logistic regression.
    """
    df["dx"] = df["Close"].diff()
    df["dxs"] = df["dx"].shift(1)
    df["pdx"] = (df["dx"] > 0).astype(int)
    df.dropna(subset=["pdx", "dxs"], inplace = True)
    dx = df["pdx"]
    dxs = df["dxs"]
    model = sm.Logit(dx, dxs).fit()
    t = model.tvalues["dxs"]
    return t
print(autoregress_logit(load_data()))


# ## Exercise 5

# In[29]:


def plot_delta(df: pd.DataFrame) -> None:
    """
    Function that takes our solution from exercise one and plots delta x, the differences in close.
    """
    df["dx"] = df["Close"].diff()
    dx = df["dx"]
    fig, ax = plt.subplots()
    dx.plot(ax=ax, color="black")
    ax.set_title("Delta x Over Time")
plot_delta(load_data())


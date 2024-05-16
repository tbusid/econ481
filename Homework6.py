#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 6

# ## Exercise 0

# In[57]:


def github() -> str:
    """
    Returns a link to my solutions on GitHub.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"


# ## Exercise 1

# In[58]:


import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import text
path = "/home/jovyan/econ-481-jupyterhub/auctions.db"
engine = create_engine(f'sqlite:///{path}')

class DataBase:
    def __init__(self, loc: str, db_type: str = "sqlite") -> None:
        """Initialize the class and connect to the database"""
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')
    def query(self, q: str) -> pd.DataFrame:
        """Run a query against the database and return a DataFrame"""
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return(df)
    def execute(self, q: str) -> None:
        """Execute statement on the database"""
        with self.engine.connect() as conn:
            conn.execute(text(q))

auctions = DataBase(path)

def std() -> str:
    """
    This function takes no arguments and returns a string containing a SQL query
    that can be run against the auctions database that outputs a table 
    that has two columns: itemId and std, the standard deviation of bids for that item.
    """

    q = """
    select itemid,
    sqrt(sum((bidamount - avg_bid) * (bidamount - avg_bid))/ (count(*) - 1)) as std
    from (select itemid,
        bidamount,
        avg(bidamount) over (partition by itemid) as avg_bid
        from bids)
    group by itemid
    having count(*) > 1
    """
    
    return auctions.query(q)
print(std())


# ## Exercise 2

# In[59]:


def bidder_spend_frac() -> str:
    """
    This function takes no arguments and returns a string containing a SQL query
    that can be run against the auctions database that outputs a table that has four columns:
    the name of the bidder, the amount the bidder spent, the amount the bidder bid,
    regardless of the outcome, and the total spend over the total bids.
    """
    q = """
    with maxbids as (select
        biddername,
        itemid,
        max(bidamount) as max_bid
        from bids
    group by biddername, itemid),
    totalspend as (select
        biddername,
        sum(max_bid) as total_spend
        from maxbids
        group by biddername),
    totalbids as (select
        biddername,
        sum(bidamount) as total_bids
        from bids
        group by biddername)
    select s.biddername, s.total_spend, b.total_bids,
        case
            when b.total_bids > 0
            then s.total_spend / b.total_bids
            else 0
        end as spend_frac
    from totalspend s
    join totalbids b on s.biddername = b.biddername
    """
    return auctions.query(q)
print(bidder_spend_frac())


# ## Exercise 3

# In[60]:


def min_increment_freq() -> str:
    """
    Some docstrings.
    """
    return


# ## Exercise 4

# In[56]:


def win_perc_by_timestamp() -> str:
    """
    Some docstrings.
    """
    return


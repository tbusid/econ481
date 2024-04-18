#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 3

# ## Exercise 0

# In[1]:


def github() -> str:
    """
    This function returns a link to my solution on GitHub.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"


# ## Exercise 1

# In[51]:


import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    This function returns a concatenated DataFrame of the Direct Emitters tab of each of those year’s EPA excel sheet.
    """
    df1, df2, df3, df4 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame() 
    urls = ['', '', '', '']
    dfs = [df1, df2, df3, df4]
    for i in range(len(years)):
        urls[i] = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_'+ years[i] +'.xlsx'
        dfs[i] = pd.read_excel(urls[i], 'Direct Emitters', skiprows = 3)
        dfs[i]['year'] = years[i]
    return pd.concat(dfs, ignore_index = True)
x = import_yearly_data(['2022', '2021', '2020', '2019'])
x.shape


# ## Exercise 2

# In[52]:


import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    This function returns a concatenated DataFrame of the corresponding tabs in the parent companies excel sheet.
    """ 
    df1, df2, df3, df4, df5 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    df6, df7, df8, df9 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    df10, df11, df12, df13 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    y = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]
    url = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'
    for i in range(len(years)):
        y[i] = pd.read_excel(url, years[i])
        y[i]['year'] = years[i]
    a = pd.concat(y, ignore_index = True)
    a = a.dropna(axis = 0, how = 'all')
    return a
d = (import_parent_companies(['2022', '2021', '2020', '2019']))
d.shape
print(d)


# ## Exercise 3

# In[5]:


def n_null(df: pd.DataFrame, col: str) -> int:
    """
    This function returns an integer corresponding to the number of null values in that column argument.
    """
    count = df[col].isnull().sum().sum()
    return count
print(n_null(d, 'FACILITY COUNTY'))


# ## Exercise 4

# In[53]:


def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function outputs a DataFrame that left join the parent companies data onto the EPA data using as join keys the year and Facility ID variables in the
    emissions data and their equivalents in the parent companies data, subsets the data to different variables, and makes all the column names lower-case.
    """
    df = pd.merge(emissions_data, parent_data, left_on=['year', 'Facility Id'], right_on=['year', 'FRS ID (FACILITY)'], how='left')
    newdf = df[['Facility Id', 'year', 'State', 'Industry Type (sectors)', 'Total reported direct emissions', 'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]
    newdf.columns = map(str.lower, newdf.columns)
    return newdf
y = clean_data(x, d)
print(y)


# ## Exercise 5

# In[56]:


def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    This function produces the minimum, median, mean, and maximum values of different variables aggregated at the level of the variables supplied in the argument.
    """
    ae = df.groupby(group_vars, as_index=True)[['total reported direct emissions', 'parent co. percent ownership']].agg(['min', 'median', 'mean', 'max'])
    ae.sort_values(by=('total reported direct emissions', 'mean'), ascending=False)
    return ae
print(aggregate_emissions(y, ['year', 'facility id']))


# In[ ]:





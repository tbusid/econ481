#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 2

# ## Exercise 0

# In[ ]:


def github() -> str:
    """
    Returns the link to my solutions on GitHub.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"


# ## Exercise 1

# In[6]:


import numpy as np
import scipy as sp
def simulate_data(seed: int) -> tuple:
    """
    Function that returns 1000 simulated observations via a certain generating process.
    """
    np.random.seed(seed)
    e = np.random.normal(0, 1, size=1000).reshape((1000,1))
    X = np.random.normal(0, np.sqrt(2), size=3000).reshape((1000, 3))
    y = np.zeros([1000,1])
    for i in range(1000):
        y[i] = (5+3*X[i,0]+2*X[i,1]+6*X[i,2]+e[i])
    return [y, X]
print(simulate_data(481))


# ## Exercise 2

# In[52]:


import numpy as np
import scipy as sp
def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    This function estimates the MLE parameters.
    """
    def neg_ll(betas: np.array) -> float: 
        beta_0, beta_1, beta_2, beta_3 = betas
        e_est = y[:, 0] - beta_0 - beta_1*X[:,0] - beta_2*X[:,1] - beta_3*X[:,2]
        negll = -np.sum(-0.5 * np.log(2*np.pi) - 0.5 * (e_est**2))

        return negll

    estimation = sp.optimize.minimize(fun=neg_ll,x0=np.array([0, 0, 0, 0]), method = 'Nelder-Mead')
    return np.array(estimation.x.reshape(-1,1))
print(estimate_mle(y, X))


# ## Exercise 3

# In[49]:


import numpy as np
import scipy as sp
def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    This function returns beta coefficients of simulated data.
    """

    def OLS(betas: np.array) -> float: 
        beta_0, beta_1, beta_2, beta_3 = betas
        e_est = y[:, 0] - beta_0 - beta_1*X[:,0] - beta_2*X[:,1] - beta_3*X[:,2]
        ols = np.sum(e_est**2)

        return ols

    estimation = sp.optimize.minimize(fun=OLS,x0=np.array([0, 0, 0, 0]), method = 'Nelder-Mead')
    return np.array(estimation.x.reshape(-1,1))
print(estimate_ols(y, X))


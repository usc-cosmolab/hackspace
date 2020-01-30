import numpy as np



def model(k, alpha, beta, gamma):
    """Returns values of alpha-beta-gamma model at given k values

    Parameters
    ----------
    k : array

    alpha, beta, gamma : float
        Parameters of model
    """


    T = (1 + (alpha*k)**beta)**gamma

    return T





def residuals(pars, data):
    """Returns data - model for given values of parameters

    Parameters
    ----------
    pars : array-like
        [alpha, beta, gamma] parameters.

    data : Data object (string)
        Data to be compared with model.
    """
    
    alpha, beta, gamme = pars
    
    
    mod = model(data.k,alpha,beta,gamma)
    res = data.P_k - mod

    return res



def objective(pars, data):
    """Objective function to miminize
    """


def get_best_fit():
    """Compute best-fit model parameters


    Returns
    -------
    pars : array-like
        Best-fit [alpha, beta, gamma] parameters 
    """

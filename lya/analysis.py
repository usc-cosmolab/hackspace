import numpy as np
from .data import get_data_transfer_function
from scipy.optimize import minimize


def model(k, alpha, beta, gamma):
    """Returns values of alpha-beta-gamma model at given k values

    Parameters
    ----------
    k : array

    alpha, beta, gamma : float
        Parameters of model
    """

    T = (1 + (alpha * k) ** beta) ** gamma

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

    alpha, beta, gamma = pars

    mod = model(data.x, alpha, beta, gamma)
    res = data.y - mod

    return res


def objective(pars, data):
    """Objective function to miminize
    """

    return (residuals(pars, data) ** 2 / data.unc ** 2).sum()


def get_best_fit():
    """Compute best-fit model parameters


    Returns
    -------
    pars : array-like
        Best-fit [alpha, beta, gamma] parameters 
    """

    data = get_data_transfer_function()
    f = lambda pars: objective(pars, data)
    res = minimize(f, (0, 7, 0))

    return res.x


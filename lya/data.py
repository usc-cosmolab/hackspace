from .conf import lya_data_path
from .theory import get_lcdm_pk
import numpy as np
import matplotlib.pyplot as plt
from .theory import get_theory_pk


class Data(object):
    def __init__(self, x, y, y_unc):
        self.x = x
        self.y = y
        self.y_unc = y_unc


def load_lya_data(filename=lya_data_path):
    """Load lyman-alpha data

    Parameters
    ----------
    filename : str
        Path to ly-a data

    Returns
    -------
    data : Data object
        K, matter power spectrum, and p(k) uncertainty arrays,
        encapsulated in Data object
    """
    x, y, y_unc = np.loadtxt(filename, unpack=True)

    data = Data(x, y, y_unc)


    return data

def plot_pk(params=None, filename=lya_data_path, color='k',marker='o',ms=5,ls='',**kwargs):
    """Plot p(k) power spectrum data and theory, with panel for residuals

    Parameters
    ----------
    params : dict or None
        Cosmological parameter dictionary; if None, then plot only data


    Returns
    -------
    fig : matplotlib Figure instance
    """

    data = load_lya_data(filename)

    if params is None:
        fig, ax = plt.subplots(1,1)
        ax.errorbar(data.x, data.y, data.y_unc, color='k',marker='o',ms=5,ls='', **kwargs)
    
    else:
        pk = get_theory_pk(data.x,params)
        res = data.y - pk
        fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})
        ax[0].errorbar(data.x, data.y, data.y_unc, color='k',marker='o',ms=5,ls='', **kwargs)
        ax[0].plot(data.x, pk, color='r',**kwargs)
        ax[1].errorbar(data.x, res, data.y_unc, color='k',marker='o',ms=5,ls='', **kwargs)
        ax[1].set_xlabel('k $Mpc^{-1}$')
        ax[0].set_ylabel('P(k)')
        ax[1].set_ylabel('Residual')
    
    return fig

def get_data_transfer_function():

    """Returns the data "transfer function" 

    Returns
    -------
    data : Data object
        Data object representing the ly-a data divided by LCDM p(k)
    """

    # Loads experimental lyman alpha P(k)
    p_data = load_lya_data()

    # Analytic P(k) from class for cold dark matter w/ corresponing k
    lcdm_pk = get_lcdm_pk(p_data.x)

    # Transfer function T(k)
    tk = np.sqrt(p_data.y / lcdm_pk)

    # Uncertanty in T(k)
    tk_unc = 0.5 * p_data.y_unc / np.sqrt(lcdm_pk * p_data.y)

    return Data(p_data.x, tk, tk_unc)


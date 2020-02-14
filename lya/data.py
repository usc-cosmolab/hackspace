from .conf import lya_data_path
import numpy as np
import matplotlib.pyplot as plt
from theory import get_theory_pk

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

def plot_pk(params=None, filename=lya_data_path):
    """Plot p(k) power spectrum data and theory, with panel for residuals
    
    Parameters
    ----------
    params : dict or None
        Cosmological parameter dictionary; if None, then plot only data


    Returns
    -------
    fig : matplotlib Figure instance
    """
    panel = (1,2)[bool(params)]
    
    data = load_lya_data(filename)
    
    fig, ax = plt.subplots(panel, 1)

    if params is None:
        ax=[ax]
        
    else:
        ax[1]
        pk=get_theory_pk(data.x,params)
    
    ax[0].errorbar(data.x, data.y, data.y_unc,
    color='k', marker="o", ms=5, ls="")

    return fig

def get_data_transfer_function():
    """Returns the data "transfer function" 

    Returns
    -------
    data : Data object
        Data object representing the ly-a data divided by LCDM p(k)
    """

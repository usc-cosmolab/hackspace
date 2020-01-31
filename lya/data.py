from .conf import lya_data_path
import numpy as np
import matplotlib.pyplot as plt

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

    data = load_lya_data(filename)

    if params is None:
        fig, ax = plt.subplots(1, 1)
        ax.errorbar(data.x, data.y, data.y_unc,
                color='k', marker="o", ms=5, ls="")

        return ax

    else:
        ... #TODO: assign this to Aryan

def get_data_transfer_function():
    """Returns the data "transfer function" 

    Returns
    -------
    data : Data object
        Data object representing the ly-a data divided by LCDM p(k)
    """

from .conf import lya_data_path


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


def get_data_transfer_function():
    """Returns the data "transfer function" 

    Returns
    -------
    data : Data object
        Data object representing the ly-a data divided by LCDM p(k)
    """

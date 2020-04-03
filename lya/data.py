import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 13
plt.rcParams["font.family"] = "stix"
plt.rcParams["text.usetex"] = True
plt.rcParams["figure.figsize"] = (6.5, 5)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["lines.color"] = "k"

from .theory import get_theory_pk
from .conf import lya_data_path, lcdm_params
from .theory import get_lcdm_pk


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


def plot_pk(
    params=None,
    filename=lya_data_path,
    point_color="k",
    marker_size=5,
    marker="o",
    line_color="tab:red",
    **kwargs
):
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

    # initialize the canvas
    fig = plt.figure()
    gspec = fig.add_gridspec(5, 1)

    # plot the error bar plot in the firs axis
    ax1 = fig.add_subplot(gspec[0:4, :])
    ax1.errorbar(
        data.x, data.y, data.y_unc, color=point_color, ls="", ms=marker_size, marker=marker, **kwargs
    )

    # add the labels
    ax1.set_xlabel("$k \\rm [h/Mpc]$")
    ax1.set_ylabel("$P(k) \\rm[Mpc/h^3]$")

    if params:
        # add new axis
        ax2 = fig.add_subplot(gspec[4, :2])

        pk = get_theory_pk(data.x, params)

        # uncomment this for testing
        # pk = data.y + 1

        res = data.y - pk

        # plot the theoretical pk in the first axis
        ax1.plot(data.x, pk, color=line_color, **kwargs)

        # plot the residuals in the second axis
        ax2.errorbar(
            data.x, res, data.y_unc, color=point_color, ls="", ms=marker_size, marker=marker, **kwargs
        )

        # add labels to the axes
        ax2.set_xlabel("$k \\rm [h/Mpc$")
        ax2.set_ylabel("Residual")

    # remove all whitespace between axes
    fig.subplots_adjust(wspace=0, hspace=0)

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
    lcdm_pk = get_lcdm_pk(p_data.x / lcdm_params["h"])

    # Transfer function T(k)
    tk = np.sqrt(p_data.y / lcdm_pk)

    # Uncertanty in T(k)
    tk_unc = 0.5 * p_data.y_unc / np.sqrt(lcdm_pk * p_data.y)

    return Data(p_data.x / lcdm_params["h"], tk, tk_unc)

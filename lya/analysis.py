def model(k, alpha, beta, gamma):
    """Returns values of alpha-beta-gamma model at given k values

    Parameters
    ----------
    k : array-like

    alpha, beta, gamma : float
        Parameters of model
    """


def residuals(pars, data):
    """Returns data - model for given values of parameters

    Parameters
    ----------
    pars : array-like
        [alpha, beta, gamma] parameters.

    data : Data object
        Data to be compared with model.
    """


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

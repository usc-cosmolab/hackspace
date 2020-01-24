from .conf import lcdm_params


def get_theory_pk(k, params):
    """Returns theoretical p(k) at z=0 given k values with given cosmo params

    Parameters
    ----------
    k : array-like
        k values at which to evaluate theoretical p(k)
    params : dict
        Cosmological parameters to pass to Class

    Returns
    -------
    pk : array
       Theoretical p(k), with proper normalization
    """


def get_lcdm_pk(k):
    """Returns theoretical p(k) for lambda-CDM cosmology

    Returns
    -------
    pk : array
        p(k) for lambda-CDM cosmology, at requested k values.
    """

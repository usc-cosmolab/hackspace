from .conf import lcdm_params
from classy import Class

def get_lcdm_pk(k):
    """Returns theoretical p(k) at z=0 given k values with given cosmo params

    Parameters
    ----------
    k : array-like
        k values at which to evaluate theoretical p(k)

    Returns
    -------
    Pk*norm : array
       Theoretical p(k), with proper normalization
    """
    
    return get_theory_pk(k,lcdm_params)

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
    Pk*norm : array
       Theoretical p(k), with proper normalization
    """
    
    # initialize class
    cosmo = Class()

    # set the class parameters
    cosmo.set({"output": "mPk", 
               "P_k_max_1/Mpc": 10.0, 
               "omega_b": params['omega_b'],
               "omega_cdm": params['omega_cdm'],
               "h": params['omega_cdm'],
               "A_s": params['A_s'],
               "n_s": params['n_s'],
               "tau_reio": params['tau_reio']})

    # run class
    cosmo.compute()

    # calculate Pk at all k values (note the normalization for k and P_k)
    h = params["h"]
    return [cosmo.pk(kk * h, 0) * h ** 3 for kk in k]
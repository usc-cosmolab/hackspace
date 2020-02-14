from .conf import lcdm_params

def get_lcdm_pk(k, params):
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
	ks = k
	params = {'delH': 4.6e-5, 'H0': 67.81, 'Omegam0': 0.3080, 'Omegab0': 0.0484, 'sigma8': 0.8149, 'ns': 0.9677, 'Tcmb0': 2.7255}

	get_theory_pk(k,params)

	return Pk

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
	
    T = transfer(k,params)
	# Equation obtained from: http://www.astro.caltech.edu/~george/ay21/eaa/eaa-powspec.pdf
    Pk = k**params['ns'] * T**2
	# Normalization obtained from: https://ned.ipac.caltech.edu/level5/March02/White/White3.html
    norm = 2927876.81638

    return Pk*norm

def transfer(k, params):
	"""Returns theoretical T(k)

	Parameters
	----------
	k: array-like
		k values at which to evaluate theoretical T(k)		
	params : dict
		Cosmological parameters used to obtain T(k)

	Returns
	-------
	Tk : array
		T(k) for lambda-CDM cosmology, at requested k values.
	"""

	omb = params['Omegab0']
	om0 = params['Omegam0']
	h = params['H0']/100.
	theta2p7 = params['Tcmb0'] / 2.7

	s = 44.5 * np.log(9.83/(om0*pow(h,2))) / np.sqrt(1.0 + 10.0 * pow(omb * h * h, 0.75))
	alphaGamma = 1.0 - 0.328 * np.log(431.0 * om0 * h * h) * omb / om0 + 0.38 * np.log(22.3 * om0 * h * h) * (omb / om0) * (omb / om0)
	Gamma = om0 * h * (alphaGamma + (1.0 - alphaGamma) / (1.0 + pow(0.43 * k* h * s, 4.0)))
	q = k * theta2p7 * theta2p7 / Gamma
	C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
	L0 = np.log(2.0 * np.exp(1.0) + 1.8 * q)
	Tk = L0 / (L0 + C0 * q * q)

	return Tk

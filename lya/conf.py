import os

# get the lya data path
path = os.path.abspath(__file__)
lya_data_path = os.path.join(os.path.dirname(path), "..", "data", "lyman-alpha.txt")

# set up comological parameters
lcdm_params = {
    "omega_b": 0.02233,
    "omega_cdm": 0.1198,
    "h": 0.6737,
    "A_s": 2.097e-9,
    "n_s": 0.9652,
    "tau_reio": 0.0540,
}

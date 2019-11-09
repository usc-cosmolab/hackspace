# CosmoLab meeting: 10/11/19

Attending: Connor Powers, Austin Cox, Aryan Rahimieh, Remy Gerras, Isabella Johansson, Vera Gluscevic, Sydney Feldman,
            Karime Maamari, Siavash Yasini, Javier Zhao, Tim Morton.

Goals for this meeting:

* Use and interpret basic python commands
* Import and use built-in python modules
* Install third-party python modules with `pip` and `conda`
* Create environments with `conda`

## Python 101

* Variable assignment
* Basic data structures
    - Lists
    - Dictionaries
    - Tuples
* Loop syntax
* Function definitions

## Python modules

* Built-in modules
* External modules

To deeper into `python` coding, see an [online python tutorial](https://docs.python.org/3/tutorial/).

## Using conda to install modules and manage environments

If `which conda` tells you that you have conda available on your system, you're good to go.
Otherwise, download and run the appropriate installer from [here](https://docs.conda.io/en/latest/miniconda.html).

In brief, for most cosmolab purposes, this command will create an environment called `cosmolab`, which probably contains most of what you need:
```conda create --name cosmolab jupyterlab numpy scipy matplotlib cython python=3.7```


--------------------------
## Cosmic microwave background / power spectrum introduction (Siavash)

Notebook [here](https://github.com/syasini/cmb_tutorials/blob/master/power_spectrum.ipynb)

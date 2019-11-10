# Nov 8, 2019

Attending: Vera Gluscevic, Tim Morton, Siavash Yasini, Aryan Rahimieh, Isabella Johansson, Karime Maamari, Remy Gerras, Sydney Feldman, Paul, Javier Zhao, Chris Lindsay, David Liu, Jack Lashner, Connor Powers. 


## More fitting a model

We also talked about chi^2, model parameter space, and constraints on parameter space from data. We plotted a "bad fit" to randomly generated data, as a warmup, and then continued exercise from previous meeting. Solutions to this are here.

## Intro to CLASS

Class is an open-source Boltzmann solver, available in a git repo [here](https://github.com/lesgourg/class_public).

Once you clone the repo, from within it run `make` in order to compile `class`, and build and install its python wrapper `classy`. If you have a mac, you may need to tweak file called `Makefile` for this to work; one common issue is that `-openmp` flag may need to be commented out if you don't wish to go through pains of installing `openmp` for now.

We briefly talked about Makefile, more in the next meeting.

Here is an example of running CLASS from the command line: `./class explanatory.ini`. File named `explanatory.ini` has input parameters for this run, and by default, outputs are saved in `output/` directory. Check them out!

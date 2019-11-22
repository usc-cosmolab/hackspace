# CosmoLab meeting: 10/4/19

We discussed the four principles Dr. Morton proposed as motivating these weekly tutorials. Why are we doing this?

* Efficiency
* Portability
* Reproducibility
* Employability

There was also a suggestion that doing hands-on activities using these tools would help motivate why we are
doing this.


## Introduction to the terminal

* Comfort with interacting with your computer by typing commands into a terminal prompt is important for a computational scientist
* Some of the most common commands you will find yourself using:
    - `pwd` (print working director; i.e., "where am I?")
    - `ls` (list contents of directory)
    - `cd <directory name>` (change directory)
    - `mkdir <new directory name>` (create a new empty directory)
    - `mv <filename> <new filename>` (move a file to a new location; i.e., rename file)
    - `rm <filename>` (remove a file)
* Each of these commands executes a program.  These programs---executable binary files---live on your filesystem
  in directories contained within the list of directories in your `$PATH` environment variable.  You can see the
  contents of your `$PATH` by executing `echo $PATH` at a command prompt.
* Whenever you type anything into a command prompt, the first "word" you type must be the name of some program
  that lives somewhere in your `$PATH`.  You can execute `which <command>` to see which version of a program
  typing `<command>` would execute, if there are multiple versions in your path---the shell (the program that
  runs in the terminal to interpret your commands) will pick the version that appears earliest in the `$PATH`.
* You can edit `$PATH` (or any other environment variable) either manually at the command line or by editing
  a file called `.bash_profile` that should live in your home directory (the location the terminal starts
  by default when you open it, or `$HOME`.)

## Miniconda

*Conda* is a very useful (and widely used) program to manage package installation and environments.  We will talk more about this
next week, but if you don't already have *conda* available on your machine (check with `which conda`), install
it by downloading the appropriate bash script installer from [here](https://docs.conda.io/en/latest/miniconda.html),
and executing it with `bash Mini<tab>`.  We briefly discussed the concept of an "environment"; again, we will
go into more detail next week on this.

## Science discussion

Dr. Gluscevic introduced and briefly discussed a paper: ["Galactic Center Gas Clouds and Novel Bounds on Ultra-Light Dark Photon, Vector Portal, Strongly Interacting, Composite, and Super-Heavy Dark Matter"](https://arxiv.org/abs/1812.10919).

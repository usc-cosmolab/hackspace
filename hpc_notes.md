#HPC = High Performance Computing

At USC, the new cluster is available to test at `discovery.usc.edu`.

Help email is `hpc-support@usc.edu`.

## Why HPC?

* You need more than your laptop can give you. (computation time, memory, disk space, etc.)
* You have trouble installing things on your laptop (the cluster is a linux system)

## Parallelization

A cluster of **nodes**, each of which has many **cores**.

* **MPI**: "message passing interface" -- Multiple copies of the same program are running.  Can be either on multiple cores on the same node, **or** across multiple nodes. 
	* Generically, you would run a program with mpi with something like `mpirun python my_parallel_script.py` (if you have mpi installed on your laptop, this kind of command would work)
	* There are different implementations of MPI, e.g. OpenMPI, Intel-MPI, etc.
* **OpenMP**: shared-memory parallelization **on a single node** across multiple cores.  Also might be called "multi-threading". 

For, e.g., cosmological inference with cobaya/class, if a node has 24 cores, you might want to have 4 copies of the program running, each using 6 threads.


## Terms of interest

* `ssh` this is a program that you use to connect to another computer.  This is the tool that we use to log on to the cluster.
	* Usually you have to type a password, but you can avoid this with "ssh keys" (google it).
	* `.ssh/config` is handy.  We can talk about that later, too.
* **submitting a batch job**: this is where you tell the cluster to do something for you.
* **SLURM**: this is the batch-submission software that manages the cluster.  You submit a job by writing a **submission script** and submitting it to the cluster with a program called `sbatch`.
* `scp`: transfer files between machines.  Uses ssh to do so. 

For example, you would have a file called `myjob.sh` that contains information that SLURM needs to submit, as well as the program that you want to run.  Then you would execute the following:

```
$ sbatch myjob.sh
```

Other useful SLURM commands: `sinfo` (shows cluster status) and `squeue -u <username>` shows status of your current jobs. 

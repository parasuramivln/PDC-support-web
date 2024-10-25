The General Algebraic Modeling System (GAMS)
The General Algebraic Modeling System (GAMS) is a high-level modeling system for mathematical programming and optimization. It consists of a language compiler and a stable of integrated high-performance solvers.


## How to use


# gams module
To load the GAMS module
ml PDC
ml gams/37.1.0

## Running using the queue system
Here is an example job script, job.sh, for running gams
#!/bin/bash
ml PDC
ml gams/37.1.0
gams inputfile.gms > outputfile.lst
Which can be submitted with
sbatch --nodes=1 -t 00:30:00 -p main -A projectname ./job.sh
where *projectname* needs to be replaced with a valid compute
time allocation.

## Running interactively
To run on an interactive node, you can allocate a node
salloc --nodes=1 -t 00:30:00 -p main -A projectname
and then run your program with the commands
srun gams inputfile.gms > outputfile.lst

## License file
Without a valid GAMS license the system will operate as a free demo system. If you own a single-user license, then you can place it in the Private subdirectory of your home folder and tell GAMS which license to use with the command line argument "license", for example:
gams license=$HOME/Private/gams-lic.txt inputfile.gms > outputfile.lst
Make sure that the license file is not readable by other users. If you own a multi-user license, then you need to use specific file access groups to control access.

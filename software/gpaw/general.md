`GPAW <https://wiki.fysik.dtu.dk/gpaw/>`_ is a density-functional theory (DFT) python code based on the projector-augmented wave (PAW) method and the atomic simulation environment (`ASE <https://wiki.fysik.dtu.dk/ase/>`_). It uses real-space uniform grids and multigrid methods or atom-centered basis-functions.

# External Links
`Official site <https://wiki.fysik.dtu.dk/gpaw/>`_


## How to use


# GPAW module
You can see which versions of gpaw are installed using
module avail gpaw

## Running GPAW
Here's an axample script to run GPAW on Dardel
#!/bin/bash
# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A 201X-X-XX
# The name of the script is myjob
#SBATCH -J myjob
# Set the partition
#SBATCH -p shared
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 0:10:00
# Number of nodes
#SBATCH --nodes 1
# Number of MPI processes per node
#SBATCH --ntasks-per-node=64
#load the gpaw module
ml add PDC/22.06
ml add gpaw/22.8.0
# Define where you have the datasets
export GPAW_SETUP_PATH=XXXX
# Run on 64 cores
gpaw -P 64 python gpaw-example.py

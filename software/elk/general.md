Elk is an all-electron full-potential linearised augmented-planewave (FP-LAPW) code. Designed to be as developer friendly as possible so that new developments in the field of density functional theory (DFT) can be added quickly and reliably.
http://elk.sourceforge.net/

## How to use

The Elk installation contained in this module was built with support for the programs and libraries Libxc and Wannier90.
To display info on which environment variables are set when loading the module, use
```
ml PDC/<version>
ml show elk/8.8.26-cpeGNU-22.06
```
To load the Elk module
```
ml PDC/<version>
ml elk/8.8.26-cpeGNU-22.06
```
The species files are found in ``EBROOTELK/species``
Examples are provided in ``$EBROOTELK/examples``

# Running on the Batch system
Sample job script to queue an Elk job with 16 MPI ranks, and 8 openMP threads

```
#!/bin/bash -l
# The -l above is required to get the full environment with modules

# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A <project name>

# The name of the script is myjob
#SBATCH -J myjob

# partition
#SBATCH -p main

# 10 hours wall-clock time will be given to this job
#SBATCH -t 10:00:00

# Number of nodes
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=16

ml PDC/<version>
ml elk/8.8.26-cpeGNU-22.06

export OMP_NUM_THREADS=8
export OMP_PLACES=cores
export OMP_PROC_BIND=false
export OMP_STACKSIZE=256M
ulimit -Ss unlimited

echo "Script initiated at `date` on `hostname`"

srun -n 16 elk > out.log

echo "Script finished at `date` on `hostname`"
```

For information on how to submit jobs on Dardel, see `Queueing jobs <https://www.pdc.kth.se/support/documents/run_jobs/queueing_jobs.html>`_ .

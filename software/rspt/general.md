The Relativistic Spin Polarized tookit (RSPt) is a code for electronic structure calculations based on the Full-Potential Linear Muffin-Tin Orbital (FP-LMTO) method. For more information see [https://www.uu.se/en/department/physics-and-astronomy/research/materials-theory/code-development](https://www.uu.se/en/department/physics-and-astronomy/research/materials-theory/code-development).

## How to use

To display info on which environment variables are set when loading the module, use
```
ml PDC/<version>
ml show rspt/20231004
To load the RSPt module
ml PDC/<version>
ml rspt/20231004
```
The binaries are found in the ``$RSPT_HOME/bin`` directory.
Examples and tests are provided in ``$RSPT_EXAMPLES``.
The manual is found in ``$RSPT_DOCS``.
```
# Running on the Batch system
Sample job script
#!/bin/bash

# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A <project name>

# The name of the script is myjob
#SBATCH -J jobname

# partition
#SBATCH -p main

# 10 hours wall-clock time will be given to this job
#SBATCH -t 10:00:00

# Number of nodes
#SBATCH -N 2

# Number of MPI processes per node
#SBATCH --ntasks-per-node=128

# Number of MPI processes
#SBATCH -n 256

ml PDC/<version>
ml rspt/20231004-cpeGNU-23.12

echo "Script initiated at `date` on `hostname`"

runs "srun -n 256 rspt" 1e-09 100

echo "Script finished at `date` on `hostname`"
```

For information on how to submit jobs on Dardel, see [Queueing jobs](https://www.pdc.kth.se/support/documents/run_jobs/queueing_jobs.html).

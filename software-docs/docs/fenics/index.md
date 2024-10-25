---
title: Information about fenics
keywords:
  - Tools
  - Mathematics
---
# Fenics

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.03 | 0.7.3 |

## General information

FEniCS is an open source software for solving partial differential equations. With FEniCS users can quickly translate scientific models into finite element code.
More information on FEniCS can be found here: https://fenicsproject.org/

## How to use

We have made a containerzied installation of FEniCS available on Dardel.
Users will have to use Singularity executable in batch job to run this containerized version of FEniCS.
Singularity is available as a module on Dardel and should be loaded in your job file to make Singularity executable available.

# Running in Batch mode
Example job script for using FEniCS on 2 nodes.

```
#!/bin/bash -l
# The -l above is required to get the full environment with modules
# Set the allocation to be charged for this job
#SBATCH -A <your allocation>
# The name of the script is specified
#SBATCH -J my_job
# Recive email notifications with any state change
#SBATCH --mail-type=ALL
# 10 hour wall-clock time will be given to this job
#SBATCH -t 10:00:00
# Set the partition for your job.
#SBATCH -p <partition>
# Number of nodes
#SBATCH --nodes=2
# Number of MPI processes per node
#SBATCH --ntasks-per-node=128
# Output and error files
#SBATCH -e error_file.e%J
#SBATCH -o output_file.o%J
# Load required modules
module load PDC
module load singularity
export OMP_NUM_THREADS=1
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/cray/pe/lib64:/usr/lib64:$LD_LIBRARY_PATH
export SINGULARITYENV_LD_LIBRARY_PATH=$LD_LIBRARY_PATH
echo $SINGULARITYENV_LD_LIBRARY_PATH
export FEniCS_CONTAINER=/pdc/software/sing_hub/fenics/2019.1.0
echo "Starting at.." ; date
# Run FEniCs
srun --mpi=pmi2 --ntasks=64 singularity exec -B /etc/libibverbs.d:/etc/libibverbs.d:ro -B /var/spool:/var/spool -B /usr/lib64:/usr/lib64:ro -B /opt:/opt:ro -B /var/opt:/var/opt:ro $FEniCS_CONTAINER bash -c "python3 <input.py>"
echo "Ending at.." ; date
```



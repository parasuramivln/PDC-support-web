---
title: Information about veloxchem
keywords:
  - Applications
  - Chemistry
---
# Veloxchem

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 1.0rc3 |

## General information

VeloxChem is a Python-based open source quantum chemistry software developed
for the calculation of molecular properties and simulation of a variety of
spectroscopies.
For more information see the [VeloxChem homepage](https://veloxchem.org/).

## How to use
This is a release candidate of VeloxChem 1.0.
For a list of features in VeloxChem, see the
[VeloxChem homepage](https://veloxchem.org/).

## Running VeloxChem
Here is an example of a job script
```
#!/bin/bash

#SBATCH -A XXXX-X-XX
#SBATCH -J my_vlx_job
#SBATCH -t 01:00:00
#SBATCH -p main

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=32

module load PDC/23.12
module load veloxchem/1.0rc3

export OMP_NUM_THREADS=16
export OMP_PLACES=cores
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

srun vlx myjob.inp myjob.out
```


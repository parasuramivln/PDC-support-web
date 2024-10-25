GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles. It provides extremely high performance compared to all other programs through custom algorithmic optimizations. More information at http://www.gromacs.org.
Several versions of GROMACS are installed at PDC. Generally, it is recommended to use the most recent version since it can be expected to be faster,
more stable and less memory demanding.
Information on how to run GROMACS on AMD GPU nodes of an HPE Cray EX cluster can be found in `How to run GROMACS efficiently on the LUMI supercomputer <https://zenodo.org/records/10683366>`_.

## How to use

GROMACS is highly tuned for quite efficient use of HPC resources.
Special assembly kernels make its core compute engine one of the fastest MD
simulation programs.
In order to use this module, you need to
```
ml PDC
ml gromacs/2021.6-cpeCray-22.06-plumed-2.7.2
```
Preprocessing input files (molecular topology, initial coordinates and
mdrun parameters) to create a portable run input (.tpr) file can be run
in a batch job by
```
srun -n 1 gmx_mpi grompp -c conf.gro -p topol.top -f grompp.mdp
```
Gromacs also contains a large number of other pre- and post-processing tools.
A list of available commands can be seen by
```
srun -n 1 gmx_mpi help commands
```
This module provides four main versions of the GROMACS suite:
* *gmx* : The MD engine binary without MPI, but with openMP threading. Useful if GROMACS is executed for preprocessing or running analysis tools on a compute node.
* *gmx_mpi* : The MD engine binary with MPI support. This is the one that researchers would use most of the time.
* *gmx_d* : Same as *gmx* above but in double precision.
* *gmx_mpi_d* : Same as *gmx_mpi* above but in double precision.
All tools from the GROMACS suite can be launched using any of the above
versions. Please note that they should be launched on the compute node(s).
Remember to *always* use in your scripts *srun* in front of the actual GROMACS
command! Here is an example script that requests 2 nodes:

```
#!/bin/bash

#SBATCH -J my_gmx_job
#SBATCH -A snicYYYY-X-XX
#SBATCH -p main
#SBATCH -t 01:00:00

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128

ml PDC
ml gromacs/2023-cpeGNU-22.06

export OMP_NUM_THREADS=1

srun -n 1 gmx_mpi grompp -c conf.gro -p topol.top -f grompp.mdp
srun gmx_mpi mdrun -s topol.tpr -deffnm gmx_md
```

In addition to the four main versions, the module contains also two auxiliary versions
* *gmx_seq* : The MD engine binary without MPI, but with openMP threading. Useful if GROMACS is executed for interactive preprocessing on a login node. This binary
can be launched without *srun*.
* *gmx_seq_d* : Same as *gmx_seq* above but in double precision.

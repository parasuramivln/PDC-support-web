CP2K is a program to perform atomistic and molecular simulations of solid state, liquid, molecular, and biological systems. For more information please visit: http://www.cp2k.org


## How to use

The CP2K installation contained in this module was built with support for the programs and libraries ELPA, Libint-CP2K, libvori, libxc, libxsmm, PLUMED, and spglib.
To display info on which environment variables are set when loading the module, use
```
ml PDC/<version>
ml show cp2k/2022.2-cpeGNU-22.06
```
To load the CP2K module
```
ml PDC/<version>
ml cp2k/2022.2-cpeGNU-22.06
```
Below follows an example job script for CP2K, for running on a single Dardel node using 16 MPI ranks and 8 threads.
You need to replace *pdc.staff* with an active project that you belong to.

```
#!/bin/bash -l

#SBATCH -J cp2k-test
#SBATCH -A pdc.staff
#SBATCH -p main
#SBATCH -t 1-00:00:00

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=16

ml PDC/<version>
ml cp2k/2022.2-cpeGNU-22.06

export OMP_NUM_THREADS=8
export OMP_PLACES=cores

srun cp2k.psmp -i inputfile.inp -o logfile.log
```

Assuming the script is named jobscriptCP2K.sh, it can be submitted using:
```
sbatch jobscriptCP2K.sh
```

It can happen that the threads exceed their stack space which results in segmentation fault. If this happens,
try increasing the stack space by adding the lines
```
export OMP_STACKSIZE=256M
ulimit -Ss unlimited
```
to the job script.
For the CP2K benchmark case
`H2O-dft-ls.NREP4.inp <https://github.com/cp2k/cp2k/blob/master/benchmarks/QS_DM_LS/H2O-dft-ls.NREP4.inp>`_
the optimal setting for running on 8 nodes on Dardel is

```
#!/bin/bash -l

#SBATCH -J cp2k-test
#SBATCH -A pdc.staff
#SBATCH -p main
#SBATCH -t 01:00:00

#SBATCH --nodes=8
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=16

ml PDC/<version>
ml cp2k/2022.2-cpeGNU-22.06

export OMP_NUM_THREADS=8
export OMP_PLACES=cores

srun cp2k.psmp -i inputfile.inp -o logfile.log
```

For using CP2K together with PLUMED, we suggest to use 128 MPI ranks and 1 thread per node

```
#!/bin/bash -l

#SBATCH -J cp2k-test
#SBATCH -A pdc.staff
#SBATCH -p main
#SBATCH -t 1-00:00:00

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1

ml PDC/<version>
ml cp2k/2022.2-cpeGNU-22.06

export OMP_NUM_THREADS=1
export OMP_PLACES=cores

srun cp2k.psmp -i inputfile.inp -o logfile.log
```

Please consult the official CP2K documentation for more details
https://www.cp2k.org/

# Known issue
If geometry optimization got stuck in first optimization step, consider adding
``PREFERRED_DIAG_LIBRARY SL``
in the ``&GLOBAL`` section.
See https://github.com/cp2k/cp2k/issues/1696 for details.


# Using cray-petsc at PDC
cray-petsc is the cray petsc library shipped with Cray systems. It includes an
optimised version of the PETSc library. There are versions for both real and
complex arithmetic.
To see which cray-petsc versions are available use the command
module avail cray-petsc


## How to use

cray-petsc on Beskow is supplied by Cray and is integrated into the
CC/cc/ftn script environment so to link programs against cray-petsc it is
only necessary to have the correct cray-petsc module loaded. For real
arithmetic, eg
module load cray-petsc/3.5.1.0
cc example.c
and for complex arithmetic, one should eg
module load cray-petsc-complex/3.5.1.0
cc example.c
The code should compile and link without needing any extra flags.

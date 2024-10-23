
# Using cray-hdf5 at PDC
cray-hdf5 is the cray hdf5 library shipped with Cray systems. It includes an
optimised version of the hdf5 library. There are versions for both serial and
parallel arithmetic.
To see which cray-hdf5 versions are available use the command
module avail cray-hdf5


## How to use

cray-hdf5 on Beskow is supplied by Cray and is integrated into the
CC/cc/ftn script environment so to link programs against cray-hdf5 it is
only necessary to have the correct cray-hdf5 module loaded. For serial, eg
module load cray-hdf5/1.8.13
cc example.c
and for parallel, one should eg
module load cray-hdf5-parallel/1.8.13
cc example.c
The code should compile and link without needing any extra flags.

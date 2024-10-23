
# Using cray-netcdf at PDC
cray-netcdf is the cray netcdf library shipped with Cray systems. It includes an
optimised version of the netcdf library. There are versions for both serial and
parallel arithmetic.
To see which cray-netcdf versions are available use the command
module avail cray-netcdf


## How to use

cray-netcdf on Beskow is supplied by Cray and is integrated into the
CC/cc/ftn script environment so to link programs against cray-netcdf it is
only necessary to have the correct cray-netcdf module loaded. For serial, eg
module load cray-netcdf/4.3.3.1
cc example.c
and for parallel hdf5, one should eg
module load cray-netcdf-hdf5parallel/4.3.3.1
cc example.c
The code should compile and link without needing any extra flags.

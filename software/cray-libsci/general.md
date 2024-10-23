
# Using cray-Libsci at PDC
cray-libsci is the cray scientific library shiped with Cray
systems. It includes an optimised version of LAPACK and SCALAPACK and
other libraries.
To see which cray-libsci versions are available use the command 
```
module avail cray-libsci

```

## How to use

cray-libsci on Beskow is supplied by Cray and is integrated into the
CC/cc/ftn script environment so to link programs against cray-libsc it is
only necessary to have the correct cray-libsci module loaded e.g.
```
module load cray-libsci/13.0.1
cc example.c
```
The code should compile and link without needing any extra flags.

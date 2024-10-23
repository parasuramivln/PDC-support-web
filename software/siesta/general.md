SIESTA is both a method and its computer program implementation, to perform efficient electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids. For more information please visit: http://departments.icmab.es/leem/siesta/


## How to use

Example run:
module add siesta/3.2-pl-5
salloc -N 1
aprun -n 32 siesta < infil.fdf

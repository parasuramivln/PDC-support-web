CVODES is a solver for stiff and nonstiff initial value problems (IVPs) for systems of ordinary differential equation (ODEs).  It is a part of sundials, see https://computation.llnl.gov/projects/sundials


## How to use

You can load the module using
```
$ module load cvodes/2.9.0
```
As an example, we can compile and link a code (here ``example.c``) after loading the module like this
```
$ mpicc  -o a.out example.c -O3 -DNDEBUG  -I/pdc/vol/cvodes/2.9.0/include -I. -L/pdc/vol/cvodes/2.9.0/lib -lsundials_cvodes -lsundials_nvecparallel -lm /usr/lib64/librt.so -L.  /pdc/vol/i-compilers/17.0.1/mkl/lib/intel64/libmkl_intel_lp64.so /pdc/vol/i-compilers/17.0.1/mkl/lib/intel64/libmkl_sequential.so /pdc/vol/i-compilers/17.0.1/mkl/lib/intel64/libmkl_core.so -lpthread -lm    -Wl,-rpath,/pdc/vol/cvodes/2.9.0/lib

```

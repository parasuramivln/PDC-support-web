NetCDF (network Common Data Form) is a set of interfaces for array-oriented data access and a freely distributed collection of data access libraries for C, Fortran, C++, Java, and other languages, see: http://www.unidata.ucar.edu/software/netcdf


## How to use

The modules are built using different versions of gcc compiler. You can check available modules using
```
$ module avail netcdf
```
For example, load one module with gcc v4.9.2 
```
$ module load gcc/4.9.2
$ module load netcdf/4.3.3.1-gcc-4.9
```
As an example, we can compile and link a code (here ``example.c``) after loading the module like this
```
$ gcc -I/pdc/vol/netcdf/4.3.3.1/gcc/4.9/include example.c

```

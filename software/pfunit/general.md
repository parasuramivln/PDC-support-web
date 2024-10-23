pFUnit is a unit testing framework enabling JUnit-like testing of serial and MPI-parallel software written in Fortran. Limited support for OpenMP is also provided in the form of managing exceptions in a thread-safe manner.
pFUnit uses several advanced Fortran features, especially object oriented capabilities, to offer a convenient, lightweight mechanism for Fortran developers to create and run software tests that specify the desired behavior for a given piece of code.
For more information see: https://github.com/Goddard-Fortran-Ecosystem/pFUnit

## How to use

To load the module for pFUnit built with the cpeCray 21.11 toolchain

# 

```
ml PDC/21.11
ml pFUnit/4.4.1-cpeCray-21.11
```
To show path and enviroment variables set by pFUnit, do

## 

```
ml show pFUnit/4.4.1-cpeCray-21.11
```
Documentation for pFUnit can be found on https://github.com/Goddard-Fortran-Ecosystem/pFUnit#building-and-installing-pfunit.
Short examples of the usage can be found on https://github.com/Goddard-Fortran-Ecosystem/pFUnit_demos. Note that not all tests can be run without modification to their files due to the need of using srun on Dardel.


# Using gcc
GCC or the `Gnu Compiler Collection <https://gcc.gnu.org/>`_ provides
a number of compilers including a C, C++ and Fortran compilers


## How to use

When compiling on Beskow the cc/CC/ftn wrappers should always be
used. Which compiler is used is determined by which PrgEnv module is
loaded. e.g. to use the gcc compiler PrgEnv-gnu needs to be loaded
e.g. by doing
```
module swap PrgEnv-cray PrgEnv-gnu
```
To use the gnu compilers gcc, g++ or gfortran should not be called
directly, but the wrappers used instead, e.g. 
```
cc hello.c
```
It is then possible to see which version of the gnu compiler is loaded using
```
cc --version
```
The versions available can be seen using 
```
module avail gcc
```
This version is default version on beskow.


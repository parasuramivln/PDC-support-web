The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers.
The library provides a wide range of mathematical routines such as random number generators,
special functions and least-squares fitting. There are over 1000 functions in total with an extensive test suite.
More information can be found here <http://www.gnu.org/software/gsl/7/>

# Licensing
The library is free software under the GNU General Public License.


## How to use

The GSL modules were built using different toolchains. You can check available modules using

# 

```
ml PDC
ml spider GSL
ml avail GSL
```
For example, to load the module for GSL library built with the cpeCray 21.11 toolchain

## 

```
ml PDC
ml GSL/2.7-cpeCray-21.11
```
To display information on what paths and environment variables are set when loading a
GSL module

## 

```
ml show GSL/2.7-cpeGNU-21.11
env | grep -i GSL
```

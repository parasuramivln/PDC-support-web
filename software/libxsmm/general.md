LIBXSMM is a library for specialized dense and sparse matrix operations as well as for deep learning primitives such as small convolutions https://github.com/hfp/libxsmm/.

## How to use

The LIBXSMM library can be built using different toolchains. You can check available modules using

# 

```
ml PDCTEST/22.06
ml spider libxsmm
ml avail libxsmm
```
For example, to load the module for the LIBXSMM library built with the cpeGNU 21.11 toolchain

## 

```
ml PDCTEST/22.06
ml libxsmm/1.17-cpeGNU-22.06
```
To display information on what paths and environment variables are used when loading a
LIBXSMM module

## 

```
ml show libxsmm/1.17-cpeGNU-22.06
env | grep -i libxsmm
```

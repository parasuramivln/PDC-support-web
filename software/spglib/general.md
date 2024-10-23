Spglib is a library for finding and handling crystal symmetries written in C https://spglib.github.io/spglib/index.html

## How to use

The Spglib library can be built using different toolchains. You can check available modules using

# 

```
ml PDC
ml spider spglib
ml avail spglib
```
For example, to load the module for the Spglib library built with the cpeGNU 21.11 toolchain

## 

```
ml PDC
ml spglib/1.16.0-cpeGNU-21.11
```
To display information on what paths and environment variables are used when loading a
Spglib module

## 

```
ml show spglib/1.16.0-cpeGNU-21.11
env | grep -i spglib
```

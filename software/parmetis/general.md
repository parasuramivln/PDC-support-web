ParMETIS is an MPI-based parallel library that implements a variety of algorithms for partitioning unstructured graphs, meshes, and for computing fill-reducing orderings of sparse matrices, see http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview


## How to use

The ParMETIS modules were built using different toolchains. You can check available modules using

# 

```
ml PDC/<version>
ml spider parmetis
ml avail parmetis
```
For example, to load the module for ParMETIS library built with the cpeCray 21.11 toolchain

## 

```
ml PDC/<version>
ml ParMETIS/4.0.3-cpeCray-21.11
```
To display information on what paths and environment variables are used when loading a
ParMETIS module

## 

```
ml show ParMETIS/4.0.3-cpeCray-21.11
env | grep -i metis
```

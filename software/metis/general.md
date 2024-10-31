METIS is a set of serial programs for partitioning graphs, partitioning finite element meshes, and producing fill reducing orderings for sparse matrices, see http://glaros.dtc.umn.edu/gkhome/metis/metis/overview


## How to use

The METIS modules were built using different toolchains. You can check available modules using

# 

```
ml PDC/<version>
ml spider metis
ml avail metis
```
For example, to load the module for METIS library built with the cpeCray 21.11 toolchain

## 

```
ml PDC/<version>
ml METIS/5.1.0-cpeCray-21.11
```
To display information on what paths and environment variables are used when loading a
METIS module

## 

```
ml show METIS/5.1.0-cpeCray-21.11
env | grep -i metis
```

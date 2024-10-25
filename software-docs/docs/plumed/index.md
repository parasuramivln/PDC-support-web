---
title: Information about plumed
keywords:
  - Applications
  - Molecular Dynamics
---
# Plumed

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 2.9.0, 2.9.2 |

## General information

PLUMED is an open source library for free energy calculations in molecular systems. More info at https://www.plumed.org/
It could be used standalone or, as it is more common, in combination with external molecular dynamics packages such as GROMACS and CP2K. For the latter case, please use the provided modules, e.g. gromacs/2024.2-cpeGNU-23.12-plumed-2.9.2 and cp2k/2024.1-cpeGNU-23.12-gpu.

## How to use

The PLUMED library can be accessed by loading the appropriate module
```
# To load the module
ml PDC
ml PLUMED/2.7.2-cpeGNU-21.11
# To show info on what path and environment variables are set by the module
ml show PLUMED/2.7.2-cpeGNU-21.11
```


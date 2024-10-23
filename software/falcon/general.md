Falcon: a set of tools for fast aligning long reads for consensus and assembly
The Falcon tool kit is a set of simple code collection which I use for studying efficient assembly algorithm for haploid and diploid genomes. It has some back-end code implemented in C for speed and some simple front-end written in Python for convenience.
More information can be found
https://github.com/PacificBiosciences/FALCON

## How to use

This software has a number of dependencies situated
on different modules namely
#. DAZZ_DB (C)
#. DALIGNER (C)
#. pypeFLOW (python module)
#. Falcon (python module)
To load the environment
```
$ module add site-python
$ module add daligner
$ module add dazz_db

```

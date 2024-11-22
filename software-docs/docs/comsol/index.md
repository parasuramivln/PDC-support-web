---
title: Information about comsol
keywords:
  - Applications
  - Fluid Dynamics
  - Finite Element Analysis
---
# Comsol

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 6.3, 6.2, 6.1, 6.0, 5.6 |

## General information


# How to use Comsol on PDC machines
KTH has a site license for Comsol Multiphysics and almost all the modules that students and employees at KTH can use for academic work. PDC users outside KTH cannot use Comsol unless they supply their own license - to run a cluster simulation you need to own a floating network license.
To see which versions of comsol are installed on any of the machines at PDC log into the machine and type
module avail comsol
You should always run comsol simulations on */cfs/klemming* file system.
Notice also that the log and temporary files are stored in $HOME/.comsol by default. In order to avoid fully disk qutoa in the home directory  (can be checked using command *fs lq ~*),  you can do in the first time likes 
```
$ rm -rf ~/.comsol  # remove the directory .comsol
$ mkdir /cfs/klemming/scratch/<u>/<username>/.comsol # replace <u>/<username> with yours
$ ln -s /cfs/klemming/scratch/<u>/<username>/.comsol ~/.comsol # replace <u>/<username> with yours
```
i.e. soft link the $HOME/.comsol to a directory on /cfs/klemming system.
You can also redirect the temporary directory to /cfs/klemming system using comsol flags *-tmpdir* and *-recoverdir* in the job script likes 
```
$ rm -rf ~/.comsol/*
$ comsol ... -tmpdir /cfs/klemming/scratch/<u>/<user>/tmp -recoverydir /cfs/klemming/scratch/<u>/<username>/rec
```
where *...* represents the other comsol flags.
More details see
http://www.comsol.com


## How to use


# Running Comsol on Dardel
To submit a job on single node (containing 128 cores), you can do so by creating a simple script (comsol_run.sh) which includes:
and submit the script on the login node:
$ sbatch comsol_run.sh
You can control number of cores by *-np* option.
**It is recommended to clear temp directory after your simulations since it can cause your storage go above quota and you lose write permissions**



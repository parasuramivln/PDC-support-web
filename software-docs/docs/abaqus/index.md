---
title: Information about abaqus
keywords:
  - Applications
  - Finite Element Analysis
---
# Abaqus

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 2024, 2021, 2019 |

## General information

Abaqus is a commercial software package for finite element analysis. The Abaqus product suite consists of three core products: Abaqus/Standard, Abaqus/Explicit and Abaqus/CAE. Abaqus/Standard is a general-purpose solver using a traditional implicit integration scheme to solve finite element analyses. Abaqus/Explicit uses an explicit integration scheme to solve highly nonlinear transient dynamic and quasi-static analyses. Abaqus/CAE provides an integrated modelling (preprocessing) and visualization (postprocessing) environment for the analysis products.

Abaqus is used in the automotive, aerospace, and industrial product industries. The product is popular with academic and research institutions due to the wide material modeling capability, and the program's ability to be customized. Abaqus also provides a good collection of multiphysics capabilities, such as coupled acoustic-structural, piezoelectric, and structural-pore capabilities, making it attractive for production-level simulations where multiple fields need to be coupled.
Abaqus was initially designed to address non-linear physical behavior; as a result, the package has an extensive range of material models. Its elastomeric (rubberlike) material capabilities are particularly noteworthy. For more details, look at SIMULIA's web page:
[http://www.simulia.com/](http://www.simulia.com/)


## How to use

```
module load abaqus
```

!!! note load PDC module
    Please note that the `PDC` module needs to be loaded before loading the `abaqus` module

# Submitting an Abaqus job on Dardel
A script for running Abaqus on Dardel  called abaqus_run.sh is shown below.

```
#!/bin/bash 
# The -l above is required to get the full environment with modules

# Set name of the job
#SBATCH -J my_job

# set the job account
#SBATCH -A <your allocation>

# 10 hours wall-clock time will be given to this job
#SBATCH -t 10:00:00

# Set the partition for your job. 
#SBATCH -p <partition>

# Number of nodes
#SBATCH -N 1

#SBATCH -e error_file.e%J
#SBATCH -o output_file.o%J


# load module abaqus v2019
module load PDC
module load abaqus/2019
# please run the following line before submitting your job and set 
# 'abaquslm_license_file' environment variable to point to a license server
# cp /pdc/software/21.11/other/abaqus/abaqus_v6.env .

# The input file
inputFile=your_input_file

# Run abaqus on 64 cores
abaqus job=$inputFile cpus=64 mp_mode=threads interactive
```

Note that this script does not include all the arguments that you can supply to Abaqus, but you should add/modify the script to suit your needs. 
You can copy this script to your home directory at PDC and save it as `abaqus_run.sh`
```
sbatch abaqus_run.sh
```
Once the job has finished, you will find the outputs in the same directory as your job submission script.

!!! note

    **The script above works for running Abaqus only on a single node containing 128 cores. Contact PDC support if you need to run on more than one node. You might be asked for proof of scaling for more than 128 cores.**

    


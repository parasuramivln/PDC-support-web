---
title: Information about lammps
keywords:
  - Applications
  - Molecular Dynamics
---
# Lammps

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 2Aug2023 |

## General information

Lammps is a molecular dynamics simulator which can model particles at various scales and is distributed by Sandia National Laboratories.
For more information see: https://www.lammps.org/

## How to use

The LAMMPS module can be loaded with
ml PDCTEST/22.06
ml lammps/15Sep2022-cpeGNU-22.06
This will add the LAMMPS bin directory to your PATH, so that LAMMPS can be started with the command :code:`lmp_mpi` or :code:`lmp_omp`.
Below is an example batch script for a LAMMPS job:
:language: text
This will run LAMMPS (:code:`lmp`) with 256 cores (2 nodes), and will read the input specified in :code:`infile` and write to :code:`outfile` in the directory the job was submitted. Submit the batch script with the :code:`sbatch` command, see also the `How to run jobs <https://www.pdc.kth.se/support/documents/run_jobs/job_scheduling.html>`_.

# More information
For more information, refer to the `LAMMPS manual <https://docs.lammps.org/Manual.html>`_.


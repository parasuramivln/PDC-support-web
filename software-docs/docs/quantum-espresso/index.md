---
title: Information about quantum-espresso
keywords:
  - Applications
  - Chemistry
  - Physics
---
# Quantum-espresso

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 7.3 |
| Dardel/cpe23.03 | 7.2, 7.3 |

## General information

Quantum ESPRESSO is an integrated suite of open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale. It
is based on density-functional theory, plane waves, and pseudopotentials.  For
more information see http://www.quantum-espresso.org and
http://docs.snic.se/wiki/Quantum_Espresso.


## How to use


# General considerations
- You should **always** use the option ``disk_io=low``. With this option the wave functions are only written at the end of the job rather than after every intermediate step. This will substantially reduce the load on the disk systems and make your job run faster.
- Also it is **NOT allowed** to run the phonon part of Quantum ESPRESSO (i.e.  ``ph.x``) on Dardel. This is because the phonon part does not seem to have the equivalent of ``disk_io=low`` and therefore creates more IO than the shared Lustre system can handle.

## Running Quantum ESPRESSO
To use this module do
ml PDC/22.06
ml quantum-espresso/7.1.0-cpeGNU-22.06
Here is an example of a job script requesting 128 MPI processes per node:
:language: text
Since OpenMP is supported by this module, you can also submit a job
requesting 64 MPI processes per node and 2 OpenMP threads per MPI
process, using the job script below. Please note that in this case
you need to specify ``--cpus-per-task``, ``OMP_NUM_THREADS``, and ``OMP_PLACES``,
and that the value of ``--cpus-per-task`` is equal to 2x ``OMP_NUM_THREADS``,
becasue AMD's simultaneous multithreading (SMT) is enabled.
:language: text


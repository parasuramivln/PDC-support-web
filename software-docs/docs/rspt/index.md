---
title: Information about rspt
keywords:
  - Applications
  - Physics
---
# Rspt

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 20231004 |
| Dardel/cpe23.03 | 20231004 |

## General information

The Relativistic Spin Polarized tookit (RSPt) is a code for electronic structure calculations based on the Full-Potential Linear Muffin-Tin Orbital (FP-LMTO) method.
https://www.physics.uu.se/research/materials-theory/ongoing-research/code-development/rspt-main

## How to use

To display info on which environment variables are set when loading the module, use
ml PDC/22.06
ml show rspt/20211004
To load the RSPt module
ml PDC/22.06
ml rspt/20211004
The binaries are found in the ``$RSPT_HOME/bin`` directory.
Examples and tests are provided in ``$RSPT_EXAMPLES``.
The manual is found in ``$RSPT_DOCS``.

# Running on the Batch system
Sample job script
:language: text
For information on how to submit jobs on Dardel, see `Queueing jobs <https://www.pdc.kth.se/support/documents/run_jobs/queueing_jobs.html>`_.


---
title: Information about score-p
keywords:
  - Tools
---
# Score-p

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 8.4-cpeGNU, 8.4-cpeCray |

## General information

Score-P Scalable Performance Measurement Infrastructure for Parallel Codes
https://www.vi-hps.org/projects/score-p

## How to use

The Score-P measurement infrastructure is a highly scalable and easy-to-use tool suite for profiling and event tracing of HPC applications.
You can check available modules of Score-P using
```
ml PDC
ml spider Score-P
ml avail Score-P
```
For example, to load the module for Score-P built with the cpeGnu 21.11 toolchain
```
ml PDC
ml Score-P/7.0-cpeGNU-21.11
```
To display information on what dependency modules are loaded, and paths and environment variables are set, when loading a
Score-P module
```
ml show Score-P/7.0-cpeGNU-21.11
```
The Score-P user guide can be found on the project's webpage https://www.vi-hps.org/projects/score-p .


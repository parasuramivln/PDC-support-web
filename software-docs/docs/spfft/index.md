---
title: Information about spfft
keywords:
  - Libraries
---
# Spfft

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 1.1.0 |
| Dardel/cpe23.03 | 1.0.6 |
| Dardel-GPU/cpe23.03.gpu | 1.0.6 |
| Dardel-GPU/cpe23.12.gpu | 1.1.0 |

## General information

Sparse Fast Fourier Transform (SpFFT) is A 3D FFT library for sparse frequency domain data written in C++ with support for MPI, OpenMP, CUDA and ROCm. For more information see the [SpFFT homepage](https://github.com/eth-cscs/SpFFT).

## How to use
You can check available SpFFT modules using
```
ml spider heffte
```
For example, load the module for the SpFFT library 1.1.0 with GPU backend
```
ml PDC/<version>
ml spfft/1.1.0-cpeGNU-23.12-gpu
```
To see what environment variables are set when loading the module
```
ml show spfft/1.1.0-cpeGNU-23.12-gpu
```


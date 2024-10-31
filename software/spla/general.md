Specialized Parallel Linear Algebra (SPLA) provides specialized functions for linear algebra computations with a C++ and C interface, which are inspired by requirements in computational material science codes. SPLA provides functions for distributed matrix multiplications with specific matrix distributions, which cannot be used directly with a ScaLAPACK interface. All computations can optionally utilize GPUs through CUDA or ROCm, where matrices can be located either in host or device memory. For more information see https://github.com/eth-cscs/spla.

## How to use

You can check available SPLA modules using
```
ml spider spla
```
For example, load the module for the SPLA library 1.5.5 with GPU backend
```ml PDC/<version>
ml spla/1.5.5-cpeGNU-23.12-gpu
```
To see what environment variables are set when loading the module
```
ml show spla/1.5.5-cpeGNU-23.12-gpu
```

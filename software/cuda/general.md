CUDA is a parallel computing platform and programming model invented by NVIDIA. It enables dramatic increases in computing performance by harnessing the power of the graphics processing unit (GPU).
More information can be found here <https://developer.nvidia.com/cuda-zone>

# Licensing
The NVIDIA CUDA Toolkit License Agreement http://docs.nvidia.com/cuda/eula/#axzz4Sc8ENX6u


## How to use

You can load the module using
```
$ module load cuda/8.0
```
As an example, we can compile a code (here ``example.cu``) after loading the module like this
```
$ nvcc -o a.out example.cu

```

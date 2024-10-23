Allinea Forge is the complete toolsuite for software development - with everything needed to debug, profile, optimize, edit and build C, C++ and Fortran applications on Linux for high performance - from single threads through to complex parallel HPC codes with MPI, OpenMP, threads or CUDA.
For more information see:
https://www.allinea.com/products/develop-allinea-forge

# Allinea DDT
Allinea DDT is the debugger for software engineers and scientists developing C++, C or Fortran parallel and threaded applications on CPUs, GPUs and Intel Xeon Phi coprocessors.
Its powerful intuitive graphical interface with automatic detection of memory bugs, divergent behavior and lightning-fast performance at all scales combine to make Allinea DDT the number one debugger in research, industry and academia.

## Allinea MAP
Allinea MAP is a profiler that shows you which lines of code are slow and gets everything else out of your way.
Whether at one process or ten thousand, Allinea MAP is designed to work out-of-the-box with no need for instrumentation and no danger of creating large, unmanageable data files.  Software engineers developing parallel and threaded applications on CPUs, GPUs and Intel Xeon Phi coprocessors rely on Allinea MAP's unrivalled capability.

## How to use

To use Allinea **DDT**/**MAP** we need to compile it with the module *allinea-forge/7.0* loaded
```
$ module load allinea-forge/7.0
```
If a change of the environment is necessary, make sure you perfom it **before** loading the **allinea-forge/7.0** module. For example
```
$ module sw PrgEnv-cray PrgEnv-intel
$ module load allinea-forge/7.0
```

# Running Allinea MAP
On Beskow the program must either be dynamically linked (using **-dynamic**) or explicitly linked with the Allinea profiling libraries.
Here is an example from the official documentation 
```
$ cd $SNIC_TMP
$ mkdir apr-test
$ cd apr-test
$ cp /pdc/vol/allinea-forge/7.0/examples/wave.c .
$ cc wave.c -o wave.x -dynamic
```
The binary ``wave.x`` is now instrumented for Allinea MAP (and DDT).
In order to run you must prepend the **aprun** command in your bash scipt or interactive run with **map --profile**. Here is a simple script that runs the example compiled above:
One can also ignore the *aprun* command **but not its options** (see above example). Allinea MAP is aware of that applications are run with aprun on Beskow.
The run will generate additional file next to the normal output of the profiled application, namely
```
<app>_<cores>p_<date-stamp>_<time-stamp>.map
```
You can open the **map** file in Allinea Forge GUI. The reuslt will look similar to this one:
:width: 500pt

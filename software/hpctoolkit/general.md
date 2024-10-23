HPCToolkit is an integrated suite of tools for measurement and analysis of
program performance on computers ranging from multicore desktop systems to the
nation's largest supercomputers. For more information please visit:
http://hpctoolkit.org/


## How to use

Below is an example of using hpctoolkit.
Load the hpctoolkit module
```
module load hpctoolkit/242f100
```
Compile your own code
```
cc -g -O3 -o myexe mycode.c
```
Get an interactive node
```
salloc -N 1 -t 01:00:00 -A ...
```
Run your code with the ``hpcrun`` command. You can find ``hpcrun``
arguments on `this page <http://hpctoolkit.org/man/hpcrun.html#section_3>`__,
and examples on `this page
<http://hpctoolkit.org/man/hpcrun.html#section_10>`__. 
```
srun -n 32 hpcrun [arguments] ./myexe
```
Generate program structure
```
srun -n 1 hpcstruct ./myexe
```
Generate performance database
```
srun -n 1 hpcprof -S myexe.hpcstruct hpctoolkit-myexe-measurements-...
```

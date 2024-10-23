
# General usage
MATLAB is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages.
In order to use Matlab you need to have a Matlab license. KTH has a site-wide license for Matlab which includes all Matlab toolboxes.

## External links
`Matlab <https://se.mathworks.com/products/matlab.html>`_
`Information on the Matlab Parallel Computing Toolbox <https://se.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html>`_
`Matlab information at the SNIC knowledge base <http://docs.snic.se/wiki/Matlab>`_

## How to use


# Getting Started with serial and parallel MATLAB
Load the matlab module by
```
ml add PDC/22.06
ml matlab/r2021b
```
In order to use MATLAB you need to have a MATLAB license. KTH has a site license that
enable academic users of PDC computers around the world (student, faculty, staff) to use MATLAB.
To access the installation of MATLAB on Dardel, please contact PDC support and request access.

## Running interactively
MATLAB can be run interactively on an allocated node. To book a
single node for one hour, type
```
salloc -N 1 -t 1:00:00 -A pdc.staff -p main
# wait for a node to be reserved
```
A typical output will look like
```
salloc: Granted job allocation 591571
salloc: Waiting for resource configuration
salloc: Nodes nid001015 are ready for job
```
Node nid001015 is now yours for the next hour, and you can log into it and
start MATLAB. On Dardel you can login to the reserved node via the login node
```
ssh -X nid001015
```
and then start MATLAB with
```
ml add PDC/22.06
ml matlab/r2021b
matlab
```
In case you do not need a full node with 128 cores, you could request
cores in the shared partition. These cores are shared with other users,
with the amount of memory provided proportional to the number of cores
awarded.
```
salloc -n 24 -t 1:00:00 -A pdc.staff -p shared
```
In the following example, a parallel pool of 24 workers is opened and
a function, parallel_example (described further below), is called
```
>> p=parpool(24)
Starting parallel pool (parpool) using the 'local' profile ... connected to 24 workers.
```
p =
Pool with properties:
Connected: true
NumWorkers: 24
Cluster: local
AttachedFiles: {}
IdleTimeout: 30 minute(s) (30 minutes remaining)
SpmdEnabled: true
>> parallel_example
t =
2.4711
ans =
2.4711
This is how parallel_example.m might look
```
function t = parallel_example
t0 = tic;
parfor idx = 1:24
A(idx) = idx;
pause(2)
end
t = toc(t0)
```

## Running parallel batch jobs
You can also submit parallel workflows to the SLURM queueing system.
The following job script allocates 16 cores on Dardel and runs one MATLAB
program. If the program contains the parpool() command and parfor loops
(as demonstrated above),
MATLAB will parallelize the computation over different cores of the node.
Update the SLURM directives to set your project ID and
the number of nodes and hours that you wish to allocate,
and save the script as ``run_matlab.sh``.
You can then submit the job with
```
sbatch run_matlab.sh
```
It is advisable to run your code with different numbers of workers to
determine the ideal number to use.

## Running multiple serial batch jobs
If you have several serial MATLAB jobs that can be run simultaneously (for
example, one MATLAB program with different input parameters), these can
be run simultaneously on a booked node (in the main partition) or on booked cores
(in the shared partition). A simple bash script for submitting multiple MATLAB jobs
on 24 cores in the shared partition of Dardel node can look like
Update the SLURM directives to set your project ID and
the number of cores and hours that you wish to allocate,
and save the script as ``run_matlab.sh``.
You can then submit the job with
```
sbatch run_matlab.sh
```

## To learn more
To learn more about the MATLAB Parallel Computing Toolbox, check out these resources:
#. `Parallel Computing Coding Examples <http://www.mathworks.com/products/parallel-computing/code-examples.html>`_
#. `Parallel Computing Documentation <http://www.mathworks.com/help/distcomp/index.html>`_
#. `Parallel Computing Overview <http://www.mathworks.com/products/parallel-computing/index.html>`_
#. `Parallel Computing Tutorials <http://www.mathworks.com/products/parallel-computing/tutorials.html>`_
#. `Parallel Computing Videos <http://www.mathworks.com/products/parallel-computing/videos.html>`_
#. `Parallel Computing Webinars <http://www.mathworks.com/products/parallel-computing/webinars.html>`_

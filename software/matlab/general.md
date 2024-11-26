# General usage
MATLAB is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages.
In order to use Matlab you need to have a Matlab license. KTH has a site-wide license for Matlab which includes all Matlab toolboxes.

## External links
- [Matlab](https://se.mathworks.com/products/matlab.html)
- [Information on the Matlab Parallel Computing Toolbox](https://se.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html)

# How to use

## Getting Started with serial and parallel MATLAB
Load the matlab module by
```
ml add PDC
ml matlab/r2024b
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
ml add PDC
ml matlab/r2024b
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
```
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
program.
```
#!/bin/bash
#SBATCH -A naissYYYY-X-XX
#SBATCH -J myjob
#SBATCH -p shared
#SBATCH -n 16
#SBATCH -t 10:00:00

# Load the MATLAB module
ml add PDC/23.12
ml matlab/r2024b

# Launch the MATLAB calculation
matlab -nosplash -nodesktop -nodisplay <  your_matlab_program.m > your_matlab_program.out
```
If the program contains the parpool() command and parfor loops
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
```
#!/bin/bash
#SBATCH -A naissYYYY-X-XX
#SBATCH -J myjob
#SBATCH -p shared
#SBATCH -c 24
#SBATCH -t 10:00:00

# Load the Matlab module
ml add PDC/23.12
ml matlab/r2024b

# Run matlab for 24 individual programs serial_program_1.m,
# serial_program_2.m ... and print output in files logfile_1, logfile_2, ...
# The input files must be in the directory where you submit this script.
# This is also where the output will be created.

for i in {1..24} ; do
    matlab -nosplash -nodesktop -nodisplay < serial_program_${i}.m > logfile_$i &
done
# This wait command must be present since otherwise the job will terminate immediately
wait
```
Update the SLURM directives to set your project ID and
the number of cores and hours that you wish to allocate,
and save the script as ``run_matlab.sh``.
You can then submit the job with
```
sbatch run_matlab.sh
```

## References on the MATLAB Parallel Computing Toolbox
- [Parallel Computing Coding Examples](http://www.mathworks.com/products/parallel-computing/code-examples.html)
- [Parallel Computing Documentation](http://www.mathworks.com/help/distcomp/index.html)
- [Parallel Computing Overview](http://www.mathworks.com/products/parallel-computing/index.html)
- [Parallel Computing Tutorials](http://www.mathworks.com/products/parallel-computing/tutorials.html)
- [Parallel Computing Videos](http://www.mathworks.com/products/parallel-computing/videos.html)
- [Parallel Computing Webinars](http://www.mathworks.com/products/parallel-computing/webinars.html)

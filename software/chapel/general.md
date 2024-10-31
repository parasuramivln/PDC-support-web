Chapel is a programming language designed for productive parallel computing on
large-scale systems.
More information can be found here https://chapel-lang.org


## How to use

You can find more information on chapel at https://chapel-lang.org/
Also you can find some nice information on how to develop using
chapel... https://hpc-carpentry.github.io/hpc-chapel/
As an example, you can compile using Chapel like
$ ml PDC/<version>
$ ml chapel
$ chpl -o hello hello.chpl
For running chapel executable, you do not need to use *srun*
as it will be executed within the executable.
An example for a batchscript can be found below...
#!/bin/bash -l
#SBATCH -A 201X-X-XX
# 10 hours wall-clock time will be given to this job
#SBATCH -t 10:00:00
# Set the partition for your job.
#SBATCH -p main
# Number of nodes
#SBATCH --nodes=2
module add PDC
module add chapel
# -nl depicts the number of nodes chapel should run on
<name of executable> -nl 2

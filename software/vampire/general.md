VAMPIRE: Atomistic simulation of magnetic materials

## How to use

Running Vampire:
Load the appropriate module:
module load vampire/5.0
For an interactive run executive:
$ srun  vampire-parallel
Or Launch a job script (vampire.run) for a background execution:
sbatch ./vampire.run
Example job script:
#!/bin/bash -l
#SBATCH -J vampire-test
#SBATCH -t 03:59:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=32
# load the vampire module
module load vampire/6.0
srun vampire-parallel


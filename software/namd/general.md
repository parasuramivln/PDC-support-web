NAMD is a molecular dynamics program

# External links
`NAMD information at the SNIC knowledge base <http://docs.snic.se/wiki/NAMD>`_


## How to use


# Running on Dardel
Example job script for regular NAMD run on 2 nodes:
#!/bin/bash -l
#SBATCH -A XXXX-XX-XX
#SBATCH -J namdjob
#SBATCH -t 00:10:00
#SBATCH --nodes=2
#SBATCH -p main
#SBATCH --ntasks-per-node=128
# load the NAMD module
ml PDC/21.11
ml NAMD/2.14
# Run namd
srun namd2 input.namd > output_file
Example job script for a 2-node shared-memory NAMD run with one
MPI process per node:
#!/bin/bash -l
#SBATCH -A XXXX-XX-XX
#SBATCH -J namdjob
#SBATCH -t 00:10:00
#SBATCH --nodes=2
#SBATCH -p main
#SBATCH --ntasks-per-node=1
# load the NAMD module
ml PDC/21.11
ml NAMD/2.14
# Run namd
srun -n 2 namd2 +ppn 31 input.namd > output_file
Example job script for a 2-node shared-memory NAMD run with 4 MPI
processes per node and explicit mapping of communication and
processing cores:
#!/bin/bash -l
#SBATCH -A XXXX-XX-XX
#SBATCH -J namdjob
#SBATCH -t 00:10:00
#SBATCH --nodes=2
#SBATCH -p main
#SBATCH --ntasks-per-node=4
# load the NAMD module
ml PDC/21.11
ml NAMD/2.14
# Run namd
srun -n 8 namd2 +ppn 7 +pemap 1-7,9-15,17-23,25-31 +commap 0,8,16,24 input.namd > output_file

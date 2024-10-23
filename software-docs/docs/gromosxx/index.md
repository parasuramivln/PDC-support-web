# Gromosxx

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.03 | 1.6.0-OMP |

## General information

GROMOS is a molecular dynamics program
GROMOS is an acronym of the GROningen MOlecular Simulation computer program package, which has been developed since 1978 for the dynamic modelling of (bio)molecules, until 1990 at the University of Groningen, The Netherlands, and since then at the ETH, the Swiss Federal Institute of Technology, in Zürich, Switzerland. Its development was driven by the research group of Wilfred van Gunsteren. Currently, the development is shared between him and the research groups of Philippe Hünenberger and Sereina Riniker at the ETH, of Chris Oostenbrink at the University of Natural Resources and Life Sciences in Vienna, Austria, and of Niels Hansen at the University of Stuttgart, Stuttgart, Germany.
Since the last official release of the GROMOS software and manual in 1996, called GROMOS96, no comprehensive release occurred till 2011. Yet the GROMOS software has seen a steady development since 1996, see e.g. [1]. The programming language has been changed from FORTRAN to C++, the documentation has been put into electronic form, and many new features have been included in the software.
To the development of the GROMOS software (since 1978) members of the research groups of Wilfred van Gunsteren (Groningen, Zürich), Philippe Hünenberger (Zürich), Chris Oostenbrink (Vienna), Niels Hansen (Stuttgart) and Sereina Riniker (Zürich) have contributed.

# External links
`GROMOS manual <https://www.gromos.net/>`_


## How to use


# Running on Dardel
The current installation of GROMOS is built with OpenMP support
enabled. This means that you can run GROMOS in parallel on a single
node by using multiple threads. The number of threads can be set using
the `OMP_NUM_THREADS` environment variable.
Unfortunately, the OMP implementation allows a maximum of 16 threads.
#!/bin/bash -l
#SBATCH -A XXXX-XX-XX
#SBATCH -J gromosjob
#SBATCH -t 00:10:00
#SBATCH --nodes=1
#SBATCH -c 16 # 16 cores
#SBATCH -p main
# set the number of threads
export OMP_NUM_THREADS=16
# load the GROMOS module
ml PDC/23.03
ml gromosXX/1.6.0-cpeGNU-23.03-omp
# Run gromos
srun srun md \
@topo topology.top \
@conf input_coord.g96 \
@fin output_coord.g96 \
@refpos refpos.rpr \
@posresspec posresspec.por \
@trc output_trajectory.trc.gz \
@tre output_energy.tre.gz \
@input config.imd > log.omd



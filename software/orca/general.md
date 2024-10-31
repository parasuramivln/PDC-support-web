ORCA is an ab initio quantum chemistry program package that contains modern electronic structure methods including density functional theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical quantum chemistry methods.
https://orcaforum.kofo.mpg.de/

## How to use

The ORCA module can be loaded with
```
ml PDC/<version>
ml orca/5.0.4
```

Below follows an example job script for ORCA

```
#!/bin/bash

# time allocation
#SBATCH -A <your-project-account>

# name of this job
#SBATCH -J orca-job

# wall time for this job
#SBATCH -t 01:00:00

# number of nodes
#SBATCH --nodes=1

# partition
#SBATCH -p main

# number of MPI processes per node
#SBATCH --ntasks-per-node=128


ml PDC/<version>
ml orca/5.0.4

/pdc/software/other/orca/5.0.4/bin/orca h2.inp > out.log
```


You need to specify an active project account and the name of your ORCA input file.
Assuming the script is named jobscriptorca.sh, it can be submitted using:
```
sbatch jobscriptorca.sh
```

Please consult the official ORCA documentation for more details

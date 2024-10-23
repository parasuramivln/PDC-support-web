ORCA is an ab initio quantum chemistry program package that contains modern electronic structure methods including density functional theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical quantum chemistry methods.
https://orcaforum.kofo.mpg.de/

## How to use

The ORCA module can be loaded with
ml PDC/22.06
ml orca/5.0.4
Below follows an example job script for ORCA
:language: text
You need to specify an active project account and the name of your ORCA input file.
Assuming the script is named jobscriptorca.sh, it can be submitted using:
sbatch jobscriptorca.sh
Please consult the official ORCA documentation for more details

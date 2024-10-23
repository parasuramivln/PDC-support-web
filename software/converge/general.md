CONVERGE is a revolutionary CFD software with truly autonomous meshing capabilities that eliminate the grid generation bottleneck from the simulation process. Notice that you should provide your own license to run converge on PDC clusters.
Please use command
module avail converge
to list all available versions and make sure that the correct version is loaded in the job script.
For more details, look at CONVERGE web page:
https://convergecfd.com/


## How to use


# Submitting a CONVERGE job on Dardel
**Important note: you need to set "shared_memory_flag" to 0 in your input file "inputs.in" to make it work on the new SS11 partition**
A sample script for running CONVERGE on Dardel called converge_run.sh is shown below.
Note that this script does not include all the arguments that you can supply to CONVERGE, but you can/should add/replace whatever you want. As it is, it will work fine for your simulations if you follow the notation properly. You can submit the job using command on Tegner
sbatch converge_run.sh


Gerris is a Free Software program for the solution of the partial differential equations describing fluid flow. The source code is available free of charge under the Free Software GPL license.
For more details, look at the Gerris wiki page:
http://gfs.sourceforge.net/wiki/index.php/Main_Page


## How to use

Load the module with
```
$ module load gerris/20131206
```

# Submitting a gerris job on Tegner
A script for running gerris on Tegner called *gerris_run.sh* is shown below.
Note that this script does not literalinclude all the arguments that you can supply to gerris , but you should add/modify the script to suit your needs. You can copy this script to your home directory at PDC and submit it using command
sbatch gerris_run.sh
Formation on how to submit jobs on Tegner, see `Job Submission on Tegner <https://www.pdc.kth.se/resources/computers/tegner/how-to/run>`_ .


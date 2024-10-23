Ansys/Fluent is a computational fluid dynamics (CFD) software. Fluent is a general-purpose CFD code based on the finite volume method on a collocated grid.   As of 2012 KTH have made a joint purchase of ANSYS (in which Fluent is one component).

# How to use Ansys/Fluent on PDC machines
In order to use ANSYS Fluent at PDC you need to:
1. Have an account at PDC.
2. Check with the Ansys license owner at your department to allow running Ansys/Fluent at PDC
3. Contact KTH if you have problems/questions with Ansys/Fluent licenses.
Use command
module load PDC
module avail fluent
to list all available versions and make sure that the correct version is loaded in the job script. If there is no same (compatible) version as that creating the .cas file, please contact PDC (support@pdc.kth.se).
For more details, look at Ansys web page:
http://www.ansys.com/


## How to use


# Submitting a Fluent job on Dardel
Before preparing your script, you need to make a journal file to give tasks to Fluent. It should be in the same directory as your job subbmission script.
# -----------------------------------------------------------

## # SAMPLE JOURNAL FILE
# read case file (*.cas) that had previously been prepared file/read-case fluent.cas
# read data file (*.dat) in case you are starting simulation from a saved file
# comment it if you start from zero
file/read-data mycase.dat
# run 10 iterations
solve/iterate 10
# write data
file/write-data results.dat
# exit fluent
exit yes
# ------------------------------------------------------------
Then you can use the following script for running Ansys/Fluent on Dardel:
Then you can submit your job using *sbatch*
sbatch fluent_run.sh


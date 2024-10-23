Nek5000 is an open-source (released under GPL) computational fluid dynamics solver based on the spectral element method and is actively developed at the Mathematics and Computer Science Division of Argonne National Laboratory. The code is written in Fortran77/C and employs the MPI standard for parallelism. More information see https://nek5000.mcs.anl.gov/index.php/Main_Page


## How to use

Here is an example script:
Where we run on 8 nodes (256 processors in total) with 30 minutes.
And submit the job using command
```
$ sbatch jet_crf.sh
```


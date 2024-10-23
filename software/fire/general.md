Fire is commercial software and PDC has 30 UPP (AST University Partnership
Program) licenses for academic users to support research and education.  The
other users must provide their own license to the software. The environment
variable ``LM_LICENSE_FILE`` should be set to point to the license server.
In order to use AVL FIRE at PDC you need to:
- Have an account at PDC.
- Contact PDC to be added to the group of Fire users (no necessary for Scania
users). When contacting us, please state which reseach project that you are
working.


## How to use

Running using jobs that have been reserved with spattach is also possible, but
more complicated and not convered here.
To run in batch mode
```
$ module add easy
$ esubmit -n 2 -t 60 ./job.sh
```
will submit a job on 2 nodes (48 cores on Povel and 16 cores on Ferlin) with a
duration of 60 minutes.
Sample job file:


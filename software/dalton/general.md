Dalton consists of two codes (Dalton and LSDalton)
with separate binaries (dalton.x and lsdalton.x)
and separete run scripts (dalton and lsdalton).
For more information see: http://daltonprogram.org

## How to use


# Dalton
To run DALTON we need two input files (one dal file for the job specification
and one mol file to specify the molecule structure and basis set). In addition
we need a run script.
To have a simple and quick toy example we will calculate the B3LYP energy of
the H2O2 molecule on 2 nodes. This calculation takes only few seconds to run.
We will use the following job specification (b3lyp_energy.dal):
together with the following molecule specification (h2o2.mol):
and the following example runscript (dalton.run):
Here we run on 2 nodes (48 processors in total).
Do not run serial calculations on Lindgren for anything other than small tests!
Now we are ready to submit the calculation
```
$ qsub dalton.run
```

## LSDalton
As an example calculation we will repeat the above example now using LSDALTON.
We will use the following job specification (b3lyp_energy.dal):
together with the following molecule specification (h2o2.mol):
and the following example runscript (lsdalton.run):


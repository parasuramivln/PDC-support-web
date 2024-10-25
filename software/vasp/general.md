The Vienna Ab initio Simulation Package (VASP) is a computer program for atomic
scale materials modelling, e.g. electronic structure calculations and
quantum-mechanical molecular dynamics, from first principles.
For more information see: http://vasp.at

# Licenses
VASP is not free software and requires a software license.
If you want to use VASP please contact us with information
of the e-mail address that you have listed in the VASP global portal.

## How to use


# General observations
- VASP is not helped by hyper-threading (64 virtual cores per compute node).
- No GPU/OpenMP-support.
- Running on fewer than 32 cores per node allocates more memory to each MPI task. This can in some cases improve performance and is necessary if your job crashes with an OOM error. See the example submit script below on how to do this correctly.

## NPAR, NCORE and NSIM
From initial testing, we recommend:
```
- NPAR = number of compute nodes
- NCORE = cores / node, typically 16,24 or 32.
- NSIM = 2
- KPAR = number of compute nodes (if applicable)
```

## How to choose the number of cores
Rule of thumb:
- 1 atom per core = Good
- 0.5 atom per core = Could work (but bad efficiency and time wasted)
- <0.5 atom per core = Don't do it
Explanation of above:
The number of bands is more important than the number of atoms, but typically
you have about 4 bands/atom in VASP.
To choose a good number of cores, you can use this checklist:
- Check how many you have in the calculation. Let's call this "NB".
- Cores = NB is best you can do.
- For better efficiency, typically 90%+, aim for at least 4 bands per core, i.e. Cores = NB/4
- If you can use k-point parallelization ("KPAR"), use it! It improves scaling a lot. You can run up to cores = #kpts * NB / 4.
- You have now determined the number of cores.
- Look at this number. Does it look "strange"? Try to adjust the number of
bands to make the number of cores more even, .e.g we don't want a prime number.
Good numbers are multiple of 4,8,12,16 etc. For example, 512 bands is better
than 501 (=3x167).
- Calculate the number of nodes necessary, e.g. 512 cores (32 cores/node) = 16 compute nodes.
- For a wide calculation with less than 4 bands per core, try decreasing the
number of cores/node to 24/c node, or even 16c/node. You may also have to do
this get memory available for each MPI rank.

## Vasp Filenames
- **vasp** : this is normal regular VASP version for calculations using >1 k-point.
- **vasp-gamma** : gamma-point only version of VASP. Use this one if you only have the gamma point. It is much faster and uses less memory.
- **vasp-noncollinear** : VASP for noncollinear and spin-orbit coupling calculations.

## BEEF functionals
This version of VASP has been compiled with support for BEEF functionals.
See https://confluence.slac.stanford.edu/display/SUNCAT/BEEF+Functional+Software.

## VASP TST Tools
The VTST extension to VASP enables finding saddle points and evaluating
transition state theory (TST) rate constants with VASP.
Full documentation can be found at http://theory.cm.utexas.edu/vtsttools/

## VTST Scripts
A number of Perl scripts are available to perform common tasks to
help with VASP calculations, and particularly with transition state finding.
These are documented at http://theory.cm.utexas.edu/vtsttools/scripts.html and the path to the scripts is added to your PATH variable
when you load the vasp/5.4.4 module.

## VASPsol
VASPsol is an implementation of an implicit solvation model that describes the effect of electrostatics, cavitation, and dispersion on the interaction between a solute and solvent.
Full documentation on how to use VASPsol can be at https://github.com/henniggroup/VASPsol/blob/master/docs/USAGE.md. In short:
- Do a vacuum calculation for your system first and save the wavefunction file WAVECAR by specifying LWAVE = .TRUE. in the INCAR file.
- Start the solvation calculation from the vacuum WAVECAR, specify ISTART = 1 in the INCAR file.
- The solvation parameters are read from the INCAR file.
- In the simplest case the only parameter that need to be set is the solvation flag LSOL = .TRUE.

## Using vdW functionals
To use one of the nonlocal vdW functionals one needs to put the file vdw_kernel.bindat into the run directory (along with INCAR, POSCAR, POTCAR and KPOINTS). This file can be copied to your directory like this:
``cp /pdc/vol/vasp/data/vdw_kernel.bindat .``

## Running Vasp
Load the appropriate module
``module load vasp/5.4.4``
Loading **vasp module** module might generate a module conflict for **cray-mpich/7.0.4**. Go ahead and do  ``module sw cray-mpich/7.0.4 cray-mpich/7.2.2`` or ``module unload cray-mpich/7.0.4`` before loading **vasp module** again.
For an interactive run execute:
``srun -n <cores> vasp``
**OR**
launch a job script (*vasp.run*) for a background execution
``sbatch ./vasp.run``
Here is an example of a job script (*vasp.run*)
If your job requires a lot of memory it can be necessary to use fewer cores per node than the available 32. Here is an example of how to do this correctly using the -N flag to aprun, where a total of 64 cores distributed over 4 nodes (16 on each) are used

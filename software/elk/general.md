Elk is an all-electron full-potential linearised augmented-planewave (FP-LAPW) code. Designed to be as developer friendly as possible so that new developments in the field of density functional theory (DFT) can be added quickly and reliably.
http://elk.sourceforge.net/

## How to use

The Elk installation contained in this module was built with support for the programs and libraries Libxc and Wannier90.
To display info on which environment variables are set when loading the module, use
ml PDC/22.06
ml show elk/8.8.26-cpeGNU-22.06
To load the Elk module
ml PDC/22.06
ml elk/8.8.26-cpeGNU-22.06
The species files are found in ``EBROOTELK/species``
Examples are provided in ``$EBROOTELK/examples``

# Running on the Batch system
Sample job script to queue an Elk job with 16 MPI ranks, and 8 openMP threads
:language: text
For information on how to submit jobs on Dardel, see `Queueing jobs <https://www.pdc.kth.se/support/documents/run_jobs/queueing_jobs.html>`_ .

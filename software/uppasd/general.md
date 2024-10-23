The Uppsala Atomistic Spin Dynamics (UppASD) software package is a simulation suite to study magnetization dynamics by means of the atomistic version of the Landau-Lifshitz-Gilbert (LLG) equation.
https://github.com/UppASD/UppASD

## How to use

The UppASD files can be accessed by loading the appropriate modules. To see which versions of UppASD are available use the command
ml avail uppasd
ml spider uppasd
To load the 6.0.2 version of the program
ml PDC/22.06
ml uppasd/6.0.2-cpeGNU-22.06
The binary is ``sd``
Examples are provided in ``$EBROOTUPPASD/examples``
The code is documented in the `UppASD manual <https://uppasd.github.io/UppASD-manual>`_ and in technical notes in the directory ``$UPPASD_DOCS``.
A tutorial with examples and exercises on atomistic spin-dynamics are contained in the `UppASD tutorial <https://uppasd.github.io/UppASD-tutorial>`_.

# Running on the batch system
Sample job script to queue an UppASD job with 16 openMP threads on cores on the shared partition of Dardel
:language: text
For information on how to submit jobs on Dardel, see `Queueing jobs <https://www.pdc.kth.se/support/documents/run_jobs/queueing_jobs.html>`_ .

## User Graphic Interface
A `Python` based `QT` GUI for the code is available at ``$EBROOTUPPASD/ASD_GUI``.
This allows for:
- Visualization of outputs via `VTK`.
- Plotting of several quantities via integrated `Matplotlib` functionalities.
- Automatic generation of input files for `UppASD`.

## Tools for preprocessing and postprocessing
A collection of scripts for preprocessing and postprocessing of UppASD input and output files can be found in ``$EBROOTUPPASD/ASD_Tools``.

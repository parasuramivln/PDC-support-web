Octopus is a scientific program aimed at the ab initio virtual experimentation on a hopefully ever-increasing range of system types. Electrons are described quantum-mechanically within density-functional theory (DFT), in its time-dependent form (TDDFT) when doing simulations in time. Nuclei are described classically as point particles. Electron-nucleus interaction is described within the pseudopotential approximation.
https://octopus-code.org/

## How to use

To use this module do
ml PDC/22.06
ml octopus/11.4-cpeGNU-22.06
Below follows an example job script for Octopus.
:language: text
Assuming the script is named jobscriptoctopus.sh, it can be submitted using:
sbatch jobscriptoctopus.sh
Please consult the official Octopus documentation for more details


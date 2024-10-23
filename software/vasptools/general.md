These scripts and their documentation are adapted from NSC:
https://www.nsc.liu.se/software/installed/tetralith/vasptools/
The scripts are generally maintained by Peter Larsson (pla@nsc.liu.se).
Brief description of the tools:
* vaspcheck: checks VASP input files for common errors
* grad2: prints a summary of VASP relaxation runs, condensed info from OUTCAR/OSZICAR
* vasp2cif: converts POSCAR/CONTCAR to CIF-compatible files for visualization
* save: use this to restart a VASP relaxation, it copies CONTCAR to POSCAR and saves intermediate files.
* supersize: makes supercells from POSCAR/CONTCAR files
* aflow/aconvasp: a high-throughput framework for VASP with associated utilities.
Some of the scripts are further documented on Peter Larsson's web page:
http://www.nsc.liu.se/~pla/vasptools/
Aflow and Aconvasp are documented here:
http://materials.duke.edu/aflow.html
If you use Aflow/aconvasp, you should cite their paper:
S. Curtarolo, W. Setyawan, G. L. W. Hart, M. Jahnatek, R. V. Chepulskii, R. H. Taylor, S. Wang, J. Xue, K. Yang, O. Levy, M. Mehl, H. T. Stokes, D. O. Demchenko, and D. Morgan, AFLOW: an automatic framework for high-throughput materials discovery, Comp. Mat. Sci. 58, 218-226 (2012).


## How to use


# A collection of useful VASP scripts
To use the VASP scripts you need to add the module
```
$ module load vasptools/0.3
```
Brief description of the tools:
* vaspcheck: checks VASP input files for common errors
* grad2: prints a summary of VASP relaxation runs, condensed info from OUTCAR/OSZICAR
* vasp2cif: converts POSCAR/CONTCAR to CIF-compatible files for visualization
* save: use this to restart a VASP relaxation, it copies CONTCAR to POSCAR and saves intermediate files.
* supersize: makes supercells from POSCAR/CONTCAR files
* aflow/aconvasp: a high-throughput framework for VASP with associated utilities.
Some of the scripts are further documented on Peter Larsson's web page:
http://www.nsc.liu.se/~pla/vasptools/
Aflow and Aconvasp are documented here:
http://materials.duke.edu/aflow.html
If you use Aflow/aconvasp, you should cite their paper:
S. Curtarolo, W. Setyawan, G. L. W. Hart, M. Jahnatek, R. V. Chepulskii, R. H. Taylor, S. Wang, J. Xue, K. Yang, O. Levy, M. Mehl, H. T. Stokes, D. O. Demchenko, and D. Morgan, AFLOW: an automatic framework for high-throughput materials discovery, Comp. Mat. Sci. 58, 218-226 (2012).
Note that vasp2cif will not preserve symmetries from VASP - the output
CIF is always in P1 symmetry. If you have the FINDSYM program by
Harold Stokes et al. installed, vasp2cif will attempt to use that to
find any symmetries. It is available on PDC by the module
```
$ module add isotropy/9.4.1
```
to use it, cite: "ISOTROPY Software Suite, iso.byu.edu."



# How to use OpenFOAM on PDC machines
OpenFOAM is a free, open source CFD software package.
See also http://www.openfoam.com and http://www.openfoam.org.
To see which versions of OpenFOAM are installed on any of the machines at PDC log into the machine and type
module avail openfoam
As the current versions of OpenFOAM are very easily to generate massive small files,  you mast consider questions before running OpenFOAM such as:
* How often do you save your solution?
* What trace/history of your iterations do you write to file(s)?
To control this behavior you need to modify the corresponding parameters in
**system/controlDict**
writeControl    timeStep;
writeInterval   10000;
i.e. specify the number of timeStep for *writeInterval* as large as possible.
Moreover, setting *writeCompression* to compressed would really do a damper on the */cfs/klemming* file system. We already know that if someone set *runTimeModifiable* to *yes*  that will have an adverse effect on performance  since OpenFOAM then will check a lot of files at every single iteration. As a result, you should adapt the simulations to the system by tweaking the following parameters:
writeCompression                    uncompressed;
runTimeModifiable                   no;
**It is highly recommended that you run OpenFoam on your project directory to avoid any disk quota problems**
See https://www.pdc.kth.se/support/documents/data_management/lustre.html for more information about the project directory


## How to use


# Running on the Batch system
sample job script


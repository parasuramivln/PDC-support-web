CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format. CFITSIO provides simple high-level routines for reading and writing FITS files that insulate the programmer from the internal complexities of the FITS format.
More information can be found here http://heasarc.gsfc.nasa.gov/fitsio/fitsio.html


## How to use

You can load the module using
```
$ module load cfitsio/3.390
```
As an example, we can compile and link a code (here ``fitscopy.c``) after loading the module like this
```
$ gcc -o fitscopy fitscopy.c `pkg-config  --cflags --libs cfitsio` -lm
$ fitscopy in.fit out.fit
```
More examples can be found at http://heasarc.gsfc.nasa.gov/docs/software/fitsio/cexamples.html


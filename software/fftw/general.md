
# Using FFTW at PDC
`FFTW <http://www.fftw.org/>`_ is a freely available library for
performing `Fast Fourier Transforms <http://en.wikipedia.org/wiki/Fast_Fourier_transform>`_. It is available as source code and
can be compiled on most platforms and generally is one of the fastest
FFT libraries on any platform.
To see which FFTW versions are available use the command 
```
module avail fftw

```

## How to use

FFTW on Beskow is supplied by Cray and is integrated into the
CC/cc/ftn script environment so to link programs against fftw it is
only necessary to have the correct fftw module loaded e.g.
```
module load fftw
cc example.c
```
The code should compile and link without needing any extra flags.

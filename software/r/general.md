
# Instructions for using R at PDC
R is a programming language and software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis. Polls, surveys of data miners, and studies of scholarly literature databases show that R's popularity has increased substantially in recent years
More information can be found at https://cran.r-project.org/

## R Packages

## List Packages
To see a list of installed packages, please type
```
> installed.packages()
```

## How to install local packages
As many packages interfere with each other it is often a good idea to
install them locally in your userspace instead.
By default, installations of R at PDC automatically sets userpath
for user installed packages to *~/.R/<CPE>/<R version>/library*
Running are you are able to see the local folder
```
$ module add R
$ R
> .libPaths()
[1] "/cfs/klemming/home/<FIRST LETTER USERNAME>/<USERNAME>/.R/23.12/4.4.0/library"
[2] "/cfs/klemming/pdc/software/dardel/23.12/other/R/4.4.0-cpeGNU-23.12/lib64/R/library"
```

## If you would like to change this path, you must first define an R folder for the packages

```
export R_LIBS_USER=<FOLDER NAME>
mkdir -p <FOLDER NAME>
```
To install packages
```
> install.packages("package name")
```
But we aware that if you are changing the local libPaths
then you need to define what libPaths you are installing
your package. In the example above, beside
not adding a libPaths, you could also do
to install packages
```
> install.packages("package name",lib=.libPaths()[1])
```

## Install global packages
Some packages are installed by default by support.
You will not have access to install yourself any global packages unless
you are a member of the support group.
instructions at http://www.bu.edu/tech/support/research/software-and-programming/common-languages/r-basics/r-faq/
In general we can add new packages directly from within R, but to be globally accessible
they must be installed in the global repository rather than your home catalogue.
```
$ module add R
$ R
> .libPaths()
[1] "/cfs/klemming/home/<FIRST LETTER USERNAME>/<USERNAME>/.R/23.12/4.4.0/library"
[2] "/cfs/klemming/pdc/software/dardel/23.12/other/R/4.4.0-cpeGNU-23.12/lib64/R/library"
```
All the packages installed at PDC where installed in the 2nd path, which is globally accessible.
To install packages
```
> install.packages("package name",lib=.libPaths()[2])
```
Which will install [package name] in R.

## How to use

R on Dardel does not work across nodes but using the cores available
on one Dardel node should suffice for all operations.
run R it using
```
$ module add R/4.1.2
$ salloc -A <your-project-ID> -N 1 -t 60 -p <partition> srun -n 8 R --no-save <[myscript]

```

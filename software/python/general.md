Multiple versions of Python are installed on PDC machines.
To see which version of Python is available by default use the command:
```
python -V
```

# Anaconda
Python has a very large number of optional packages for
large-scale data processing and scientific computing
which are not available in the default system Python.
Many of these packages can be found in the
enterprise-ready Anaconda Python distribution,
which is installed as modules on Dardel.
To list available Anaconda modules, type:
```
$ ml PDC
$ ml av anaconda3
```

For example, to load Anaconda version 2024.02.1 for Python 3.11, type:
```
$ ml anaconda3/2024.02-1-cpeGNU-23.12
```

After loading an Anaconda module, the Python version can be printed by:
```
$ python --version
Python 3.11.7
```
The conda package manager can be used to list the packages installed in a given Anaconda module:
```
$ conda list
```
Available Anaconda environments can be listed by:
```
$ conda info --envs
```
If you need a package which is not available in any of the installed Anaconda
modules or environments, either contact PDC support or follow one of the options described below.

## Activating the base environment
Loading the Anaconda3 module does not automatically activate the "base" environment.
To activate the base environment, you can create a script that contains the following
lines

If you save this script as ``conda.init.sh`` and then :
```
$ source conda.init.sh
```
The base environment will be activated, as indicated by ``(base)`` in front of your
bash prompt.

## Creating your own Python environment
If you create your own conda environment you would have full control and
install everything you would want into that environment. For example
you can create a conda environment under your Klemming folder:
```
ml PDC
ml anaconda3/2024.02-1-cpeGNU-23.12
source conda.init.sh
conda create --name my-conda-env
conda activate my-conda-env
conda install <package-name>
```
Please note that by default the conda environment will be stored in the
``.conda`` folder in your home directory. If you would like to store the conda
environment elsewhere, you can use the ``--prefix`` flag to specify the path
when creating the environment.

## Installing your own Anaconda/Miniconda
If you need full control over your Python installation, we recommend that you
install your own Anaconda or Miniconda distribution, which is
relatively easy. The Anaconda
distribution is rather large, while Miniconda is much more lightweight.
Follow these links to find installation instructions for
`Anaconda <https://docs.anaconda.com/anaconda/install/>`_
and `Miniconda <https://conda.io/miniconda.html>`_, respectively.

## Installing Python packages using pip
Another option for installing packages which are missing from the available Anaconda
modules (and their conda environments) is to install them locally with `pip`:
```
$ ml PDC
$ ml anaconda3/2024.02-1-cpeGNU-23.12
$ pip install --user <package-name>
```
This should install the package locally under ``~/.local/lib/[.....]``.
If you would like to install your local package in a path other than ``~/.local/lib/``,
you can use the ``PYTHONUSERBASE`` environment variable to specify the installation directory
for Python packages that are installed with the ``--user`` flag.

## Using Anaconda Python on interactive node
On Dardel, you instead run Python on the allocated interactive node using
the srun command:
```
$ salloc -A <your-project-ID> -t 1:0:0 -n 1 -p shared
$ ml PDC
$ ml anaconda3/2024.02-1-cpeGNU-23.12
$ srun -n 1 python some_script.py
```
```
## Using Anaconda Python in batch job
#!/bin/bash -l
# The -l above is required to get the full environment with modules
# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A snic20XX-X-XX
# The name of the script is myjob
#SBATCH -J myjob
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 1:00:00
# Number of tasks
#SBATCH -n 1
# Job partition
#SBATCH -p shared
# load the anaconda module
ml PDC
ml anaconda3/2024.02-1-cpeGNU-23.12
# if you need the custom conda environment:
conda activate my-conda-env
# execute the program
srun -n 1 python some_script.py
# to deactivate the Anaconda environment
conda deactivate
```

## How to use


# Load the Anaconda module
To list all available Anaconda modules on Dardel, type:
```
$ module load PDC
$ module load pdc-anaconda3/2021.05
```
After loading an Anaconda module, there are information on how to use the anaconda module:
*JUST LOADING THIS MODULE DOES *NOT* CHANGE THE PYTHON VERSION, NOR ENABLES
ANY EXTRA PYTHON MODULES. This module makes available the 'conda' command, with which users can create named anaconda environments and then activate them.
To create and use a customized environment use 'conda create ...' and
then 'conda activate ...' (see example below)*.

## Create your own environment
We recommend that you create a ``~/.condarc`` file with the following lines:
pkgs_dirs:
- /cfs/klemming/<project>/username/conda-dirs/pkgs
envs_dirs:
- /cfs/klemming/<project>/username/conda-dirs/envs
Remember to replace ``<project>`` by your project direction and ``username`` by your username.
Then you can create your own conda environment by the following command.
```
$ mkdir -p /cfs/klemming/<project>/username/conda-dirs/pkgs
$ mkdir -p /cfs/klemming/<project>/username/conda-dirs/envs
$ conda create --prefix /cfs/klemming/<project>/username/conda-dirs/envs/my-conda-env python=3.8
```
Notice that replace ``<project>`` by your project direction and ``username`` by your username as that in the ``~/.condarc``.
After the environment is created you can activate it by:
```
$ conda activate my-conda-env
(my-conda-env)$ python ...
```
To deactivate your environment or the base environment, use ``conda deactivate``.


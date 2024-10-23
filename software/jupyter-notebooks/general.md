Jupyter Notebooks is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
This documentation demonstrates
how you can start a Jupyter server either on a Beskow or Tegner login node
(for light-weight calculations and to manage SLURM jobs) or on a
Tegner compute node, which you can then connect to from your local
browser in order to do interactive work in a notebook.

# External Links
https://jupyter.org/


## How to use

To connect from your browser to a Jupyter Notebook server running on a Beskow
login or compute node you need to follow a few steps.
First of all, you have to make sure that the connection between your browser
and the Jupyter server running at PDC is secure.
When that is done, you can start Jupyter on the login node and connect to it
from your browser. Note that Jupyter can not be run on a compute node
since Beskow compute nodes have limited network access (this is however
possible on Tegner).

# Security
It is imperative that you follow the following steps before using Jupyter on Beskow:
1. Generate a Jupyter configuration file under ``$HOME/.jupyter``
2. Set a strong password for Jupyter
3. Set up a self-signed certificate with ``openssl``
This will ensure a secure connection between your browser and the Jupyter server. Note that you only need to do this once on either Tegner or Beskow, since
the same configuration files will work on both clusters.

## Generating a Jupyter configuration file

## Start by logging in to Beskow and loading an Anaconda module (which versions are available can be found by ``module avail anaconda``)

```
ssh <username>@beskow.pdc.kth.se
module load anaconda/py37/5.3  # or anaconda/py27/5.3 for Python2.7
```

## Now create a configuration file by

```
jupyter notebook --generate-config
```
This command will create the Jupyter folder `$HOME/.jupyter`, and create the
notebook configuration file ``jupyter_notebook_config.py`` in this folder.
It will contain many lines with possible configuration options,
but initially they will all be commented out (prefixed with ``#``).

## A first option to add to this file is

```
c.NotebookApp.open_browser = False
```
which will let Jupyter only start the server without attempting to open
a browser.

## Setting a Jupyter password
For security reasons you should choose a strong Jupyter password.
The main method to set the password is by using the command
```
$ jupyter notebook password
```
The entered password will be saved in hashed form in a second
configuration file:
``$HOME/.jupyter/jupyter_notebook_config.json``.
You can also prepare a hashed password manually in an IPython session
and enter it into your ``jupyter_notebook_config.py`` config file
as detailed in the `official documentation <https://jupyter-notebook.readthedocs.io/en/stable/public_server.html>`_,
but note that the configuration options stored in the .json file take precedence over
ones stored in the .py one.

## Setting up a self-signed certificate
You should also use SSL with a web certificate to enable connecting to the notebook via https,
so that your hashed password is not sent unencrypted by your browser.
To generate the certificate, go to your ``Private`` folder in your AFS home directory and
use the ``openssl`` command
```
cd $HOME/Private
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem
```
This will generate a keyfile (``mykey.key``) and a certificate file (``mycert.pem``).
You will then need to set the following two flags in your config file ``jupyter_notebook_config.py``
(adjust according to your home directory)
```
c.NotebookApp.certfile = u'/afs/pdc.kth.se/home/<initial>/<username>/Private/mycert.pem'
c.NotebookApp.keyfile = u'/afs/pdc.kth.se/home/<initial>/<username>/Private/mykey.key'
```

## Running Jupyter on the login node
When all configuration steps have been done, you're ready to start using
Jupyter on the Beskow login node for managing Slurm jobs or to do
light-weight pre- and post-processing work.
To run Jupyter on the login node
first log in to Beskow and launch Jupyter
```
$ ssh username@beskow.pdc.kth.se
$ jupyter-notebook --no-browser
```
The output will show a line similar to
```
[I 14:16:11.737 NotebookApp] The Jupyter Notebook is running at:
[I 14:16:11.737 NotebookApp] https://localhost:8888/
```
Next set up an ssh tunnel so that connections to a port on your local
machine are forwarded to a port on Beskow. In this case, the port
Jupyter is using is on the login node. The port that you use locally is
independent of the remote port but it typically makes sense to use the same
port number. Provided that Jupyter is running on port 8888 (if 8888 is
taken, a higher port will be automatically chosen and reported in the
output), the following command will then forward traffic on the local port
8888 to the remote port 8888
```
$ ssh -N -L 8888:localhost:8888 username@beskow.pdc.kth.se
```
The -N option tells ssh that no remote commands will be executed which is
useful for port forwarding, and the -L option lists the port forwarding
configuration. To let ssh run in the background one can add the -f option,
so the local tunnel-enabling terminal remains usable.
Now copy the https link over to your browser. The browser will likely
complain that your certificate is not secure or not recognized (since it's
self-signed), but tell it to proceed anyways. After entering your Jupyter
password you can start working with notebooks on Beskow!
For an example on how to submit and monitor Slurm jobs from a notebook,
and analyze job output on-the-fly, have a look at `this example notebook
<https://github.com/PDC-support/jupyter-notebook/blob/master/2-slurm-analysis.ipynb>`_.

## Adding kernels, modules or libraries
If you need some library you can either install your own conda environment with jupyter notebook and the libraries you need. Then you load that one instead, or if it is not too big of a library or very commonly used we could add it to the default environment.

## Installing Jupyter on your own computer
You may wish to develop notebooks locally before copying them to PDC.
In this case you will need to install Jupyter on your own computer. If you use Anaconda,
you should already have Jupyter installed. Otherwise, please follow the installation
instructions in the `official Jupyter documentation <https://jupyter.org/install>`_.

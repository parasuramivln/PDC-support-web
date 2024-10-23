MultiNest is a Bayesian inference tool.
For more information visit the
`MultiNest website <http://ccpforge.cse.rl.ac.uk/gf/project/multinest/>`_.

# Appropriate citation
Please cite the following publications if you use MultiNest: `arXiv:0704.3704 <http://arxiv.org/abs/0704.3704>`_ , `arXiv:0809.3437 <http://arxiv.org/abs/0809.3437>`_, and `arXiv:1306.2144 <http://arxiv.org/abs/1306.2144>`_.

## How to use


# Submitting a multinest job on Tegner
A script for running multinest on Tegner called multinest_run.sh is shown below.
Note that this script does not include all the arguments that you can supply to multinest , but you should add/modify the script to suit your needs. You can copy this script to your home directory at PDC and save it as multinest_run.sh.
sbatch multinest_run.sh
In this example, we ask two nodes for one hour using the *sbatch* command. When the queuing system has processed our request and allocated the node the script steps into action.
Formation on how to submit jobs on Tegner, see `Job Submission on Tegner <https://www.pdc.kth.se/resources/computers/tegner/how-to/run>`_ .

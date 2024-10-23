`PhyloBayes-MPI <http://megasun.bch.umontreal.ca/People/lartillot/www/downloadmpi.html>`_ is a Bayesian software for phylogenetic reconstruction
using mixture models.

# External Links
`Official site <http://www.atgc-montpellier.fr/phylobayes/>`_
`GitHub <https://github.com/bayesiancook/pbmpi>`_


## How to use

Phylobayes is a Bayesian Monte Carlo Markov Chain (MCMC) sample for phylogenetic reconstruction.
Compared to other phylogenetic MCMC samplers, the main distinguishing feature of PhyloBayes is
the underlying probabilistic model, CAT. CAT is an infinite mixture model accounting for site-specific
amino-acid or nucleotide preferences. It is well suited to phylogenomic studies using large
multigene alignment.
After adding the module PhyloBayes can be run
```
module load PDC
module load Phylobayes-MPI
```
with the following example command
```
salloc -N 2 -t 15:00:00 aprun -n 64 pb_mpi -f -d convo9849.ali -cat -gtr -dgam 4 -dc catgtrconvo
```
Example data for this command can be found in
```
/pdc/vol/phylobayes/1.5a/data
```

NOT

## How to use

General instructions for using MatConvNet can be found `here <http://www.vlfeat.org/matconvnet/>`_.
In order to use it on PDC's systems cuda and matlab needs to be loaded:
module load cuda/8.0
module load matlab/r2017a
module load matconvnet/1.0
Next you can start Matlab or run any script that uses MatConvNet, e.g.
matlab -nodisplay
> run vl_setupnn
> vl_testnn('gpu', true)

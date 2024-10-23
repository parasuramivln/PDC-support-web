The ZenDNN (Zen Deep Neural Network) Library accelerates deep learning inference applications on
AMD CPUs.
More information can be found here https://developer.amd.com/zendnn/


## How to use

Tensorflow over zenDNN can be accessed by loading the appropriate module.
module load PDC
module load TF_ZenDNN/TF_v2.7_ZenDNN_v3.2_Python_v3.8
The zenDNN library does not implement training of neural networks yet, in order to activate the
vanilla training implemented in Tensorflow the following environmental variable needs to be set:
export ZENDNN_INFERENCE_ONLY=0
The number of threads that zenDNN uses can be controlled via OMP_NUM_THREADS.
For information on zenDNN visit https://developer.amd.com/zendnn/

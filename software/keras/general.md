Keras is a high-level neural networks API, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

## How to use


# Keras is build upon tensorflow. The package can be loaded in the following way:

```
$ module add cudnn/5.1-cuda-8.0
$ module load anaconda/py35/4.2.0
$ source activate tensorflow1.3
$ python
$ from keras.models import Sequential
$ rm -Rf /tmp/.keras
$ source deactivate
```
(6th step is typed after you close the python)

## If you intend to use keras with python 2.7, change the second line from the above to:

```
$ module load anaconda/py27/4.2.0

```

Boost provides free peer-reviewed portable C++ source libraries.
For more information, see: http://www.boost.org

## How to use

Load the module with
```
$ module load Boost/1.75.0-cpeGNU-21.09
```
The module prepends ``$BOOST_HOME/lib`` to ``LD_LIBRARY_PATH``
and sets ``BOOST_HOME``.
The include directory is then under ``$BOOST_HOME/include``.
As an example, we can compile and link a code (here ``hello.cpp``) like this
```
$ module load PDC
$ module load Boost
$ CC -I$BOOST_HOME/include hello.cpp -L$BOOST_HOME/lib -lboost_system
```

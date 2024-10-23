
# About ROOT
ROOT is a framework for data processing, born at CERN, at the heart of the research on high-energy physics. Every day, thousands of physicists use ROOT applications to analyze their data or to perform simulations. With ROOT you can:
1. **Save data**
You can save your data (and any C++ object) in a compressed binary form in a ROOT file. The object format is also saved in the same file: the ROOT files are self-descriptive. Even in the case the source files describing the data model are not available, the information contained in a ROOT file is be always readable. ROOT provides a data structure, the tree, that is extremely powerful for fast access of huge amounts of data - orders of magnitude faster than accessing a normal file.
2. **Access data**
Data saved into one or several ROOT files can be accessed from your PC, from the web and from large-scale file delivery systems used e.g. in the GRID. ROOT trees spread over several files can be chained and accessed as a unique object, allowing for loops over huge amounts of data.
3. **Mine data**
Powerful mathematical and statistical tools are provided to operate on your data. The full power of a C++ application and of parallel processing is available for any kind of data manipulation. Data can also be generated following any statistical distribution and modeled, making it possible to simulate complex systems.
4. **Publish results**
Results can be displayed with histograms, scatter plots, fitting functions. ROOT graphics may be adjusted real-time by few mouse clicks. Publication-quality figures can be saved in PDF or other formats.
5. **Run interactively or build your own application**
You can use the Cling C++ interpreter for your interactive sessions and to write macros, or you can compile your program to run at full speed. In both cases, you can also create a graphical user interface.
6. **Use ROOT within other languages**
ROOT provides a set of bindings in order to seamlessly integrate with existing languages such as Python, R and Mathematica.
See https://root.cern.ch for further details

## How to use


# Using ROOT
Load a specific version for use
```
module load ROOT/6.06.00
```

## Testing ROOT tests
`The Official Documentation <https://d35c7d8c.web.cern.ch/how/running-root-tests>`_ describes the following tests categories defined within the CTest framework:
#. ROOT basic tests delivered in $ROOTSYS/test
#. ROOT tutorials delivered in $ROOTSYS/tutorials
#. ROOTTEST tests that can be downloaded from `roottest repository <https://root.cern.ch/gitweb?p=roottest.git>`_  by issuing ``git clone http://root.cern.ch/git/roottest.git``

## Running tests using an existing installation produced by classic configure/make
Since the ROOTConfig.cmake file is not created when building with ``configure / make``. Also the cmake modules do not get installed. In this case we need to tell cmake where to find these.
Running the ROOTTEST tests
```
$ mkdir <test_here_dir>
$ cd <test_here_dir>
$ cmake ../roottest -DCMAKE_MODULE_PATH=${ROOTSYS}/etc/cmake\;<root-sources-dir>/cmake/modules
$ ctest -j8$ ctest -j8
```

## Running tests from the build directory (CMake)
Testing is not enabled by default when configuring the ROOT build. Enabling is done by the option testing and the option roottest to add the ROOTTEST tests to the test suit. The basic instructions are:
```
$ mkdir <builddir>
$ cd <builddir>
$ cmake -Dtesting=ON -Droottest=ON <root-sources-dir>
$ cmake --build
$ ctest -j24
```
You can select a subset of tests by using the `-R <regexpr>` and see the test output by adding `-V` to the `ctest` command. See the complete set of options of ctest (link is external)
Running tests using an existing installation produced by CMake

## Results running roottest on Tegner
The testroot run on 1/8/24 cores on Tegner with the following results
1. Running on **24 cores, 58% tests passed, 454 tests failed out of 1070**. Please refer to the :download:`log file <files/roottest_tegner_j24.log>` for further details. Label Time Summary
* cling         =  92.61 sec
* regression    =  92.61 sec
* roottest      =  92.61 sec
* tutorial      = 903.86 sec
* **Total Test time** (real) = **473.59 sec**
2. Running on **8 cores, 58% tests passed, 454 tests failed out of 1070**. Please refer to the :download:`log file <files/roottest_tegner_j8.log>` for further details. Label Time Summary
* cling         = 586.35 sec
* regression    = 586.35 sec
* roottest      = 586.35 sec
* tutorial      = 1661.01 sec
* **Total Test time** (real) = **623.45 sec**
3. Running on **single core, 58% tests passed, 454 tests failed out of 1070**. Please refer to the :download:`log file <files/roottest_tegner_j1.log>` for further details. Label Time Summary
* cling         =  53.77 sec
* regression    =  53.77 sec
* roottest      =  53.77 sec
* tutorial      = 684.57 sec
* **Total Test time** (real) = **2448.57 sec**

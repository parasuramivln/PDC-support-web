Cbc (Coin-or branch and cut) is an open-source mixed integer programming solver.  More information can be found here <https://projects.coin-or.org/Cbc>


## How to use

You can load the module using
```
$ module load cbc/2.9
```
As an example, we can run *cbc* for a LP problem like this 
```
$ cbc test.lp solve solu test.sol

```

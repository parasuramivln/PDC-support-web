SageMath is a free open-source mathematics software system licensed under the GPL.
For more details, look at the sage web page:
http://www.sagemath.org


## How to use


# Running sage on an interactive node on Tegner
You can book a compute node for interactive running sage. The command to do this is *salloc* e.g. 
```
tegner$ salloc --nodes=1 -t 1:00:00 -A <project>
salloc: Granted job allocation 2364
salloc: Waiting for resource configuration
salloc: Nodes t02n01 are ready for job
```
which will book one computer node (*t02n01.pdc.kth.se* for this case) one hour and *project* should be your projec name. And then from your local compute to login on the computer node and run sage using commands likes 
```
(open a new xterm on your local computer)
local$ ssh -Y username@t02n01.pdc.kth.se #username/node should be changed to yours
t02n01$ module add sage/7.0
t02n01$ sage
```
Formation on how to run program interactively on Tegner, see https://www.pdc.kth.se/resources/computers/tegner/how-to/run .

## Submit a sage job on Tegner
Let’s use the following example for a sage job. The sage script called *test.sage* includes all commands will be run.
:language: text
And then creat a simple job script (e.g. *sage_run.sh*) which includes:
:language: text
Submit it from Tegner's login node
$ sbatch sage_run.sh
In this example, we requested one node for one hour to run the sage script. After finish the job, the result
[x == -2, x == -1]
should be redirected to the file *my_output_file*
Formation on how to submit jobs on Tegner, see `Job Submission on Tegner <https://www.pdc.kth.se/resources/computers/tegner/how-to/run>`_ .


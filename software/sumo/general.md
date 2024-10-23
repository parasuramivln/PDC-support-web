SUMO (Simulation of Urban MObility) is an open source, highly portable, microscopic road traffic simulation package designed to handle large road networks.
More information can be found here http://sumo.dlr.de/


## How to use


# Running interactively
SUMO ran interactively on an allocated node. To book a  single node for one hour, type
```
$ salloc -A <your-project> -N 1 --time 1:0:0
```
A typical output will look like
```
salloc: Granted job allocation 591571
salloc: Waiting for resource configuration
```
The node name can be checked using the following command
```
$ echo $SLURM_NODELIST
t02n43
```
Node t02n43 is now yours for the next hour, and you can log into it and
start *SUMO* by (add -X to ssh if you want to run the SUMO GUI)
```
(Open a new terminal on the local computer and login from there)
local_computer$ ssh -X <your-username>@t02n43.pdc.kth.se
t02n43 $ module add sumo/1.2.0
t02n43 $ sumo-gui
```
A sample python script shows how to use the TraCI (Traffic Control Interface) for SUMO
And then run the python script on the computer node using command
```
t02n43 $ python run_sumo_traci.py
```


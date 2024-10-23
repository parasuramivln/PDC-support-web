LS-DYNA is a commercial general-purpose finite element program capable of simulating complex real world problems. Users must provide their own license to the software.
To see which versions of LS-DYNA are installed on any of the machines at PDC log into the machine and type 
```
module avail ls-dyna
```
More details about the software, see
http://www.lstc.com/products/ls-dyna


## How to use


# Submitting a LS-DYNA job on Dardel
A script for running LS-DYNA in MPI mode on Dardel called lsdyna_run.sh is shown below.
Note that this script does not include all the arguments that you can supply to LS-DYNA, but you should add/modify the script to suit your needs.
Firstly, you need to start the license server:
cp -r /pdc/software/21.11/other/ls-dyna/license_manager /cfs/klemming/home/<u>/<username>
# replace <username> with your username and <u> with the first letter of the username
cd license_manager
./lstc_server -l "LS-Dyna_Log_`date +%F"_"%H%M`"
**Important note: The license above belongs to a group of KTH users. You are NOT allowed to use it if you do not belong to that group**
**Also please contact PDC support if you want to run your own license server on Dardel as it might interfere with the other LS-DYNA server**
Then you can submit the job using command *sbatch*
sbatch lsdyna_run.sh
In case you want to disable your license server, use the LS-DYNA command *server_kill* to kill the process of license server
cd license_manager
./server_kill


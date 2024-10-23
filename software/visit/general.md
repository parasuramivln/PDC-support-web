
# How to use VisIt on PDC machines
VisIt is an open Source, interactive, scalable, visualization, animation and analysis tool.  VisIt contains a rich set of visualization features to enable users to view a wide variety of data including scalar and vector fields defined on two- and three-dimensional (2D and 3D) structured, adaptive and unstructured meshes. More information see
https://wci.llnl.gov/simulation/computer-codes/visit/
To see which versions of VisIt are installed  at PDC log into the machine and type
module avail visit
We recommend using the latest version.

## How to use


# Install local client
Download and install the 3.2.2 client for your operating system from https://visit-dav.github.io/visit-website/releases-as-tables/. It is important that the client version matches the server version on the cluster.

## Configure client
Start the client and navigate to Options>Host profiles>New Host. In the Host Settings tab fill in the following:
=================================== =========================================================
Field                               Value
=================================== =========================================================
Remote host name                    dardel.pdc.kth.se
Path to VisIt installtion           /pdc/software/22.06/other/visit/3.2.2
Username                            <Your PDC username>
Tunnel data connection through SSH  yes
SSH command                         ssh
=================================== =========================================================
Go to the Launch Profiles tab and select New Profile. Give it a name, such as "CPU". Go to the "Parallel" tab and check Launch parallel engine and enter the following:
=================================== =========================================================
Field                               Value
=================================== =========================================================
Parallel launch method              sbatch/srun
Partition / Pool / Queue            main
Number of processors                128
Bank / Account                      <Name of allocation at PDC>
Time Limit                          00:20:00
=================================== =========================================================
Go to the Advanced tab and check Launcher arguments, and enter:
--cpus-per-task=1
Now the settings are done! Press Apply and then Dismiss.

## Run visualization
To visualize data on Dardel, navigate to Open file... and choose dardel.pdc.kth.se instead of localhost. Now you should see list of files in your home directory on Dardel. Select the file you want to visualize and click OK. Select the profile, and modify the parameters if necessary, then click OK again.
Now VisIt puts a job in the queue and waits until it is started. Once the job starts, you can begin to visualize! Select plots and click Draw. The rendering will be done on the cluster, and then sent to your local client for display.
To view the status of the remote compute engine on the cluster, navigate to File>Compute engines... Here you can also stop the job by clicking on Close engine.
The latest visualization will be kept in your client even if the job hits the time limit or is closed. If you make some changes to the plots and press Draw, you will be asked if you want to start a new job.

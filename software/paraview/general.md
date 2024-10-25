Paraview uses a client/server model to do parallel visualisation, and has a
flexible way to connect the client (which normally runs on  your local computer
i.e. the one your keyboard is connected to) to the server (which can run in
parallel on PDC machines).  For more information see: http://www.paraview.org


## How to use


# Install client
Download and install Paraview 5.11.1 on your local workstation. Sources and installers for various operating systems are available here: https://www.paraview.org/download.
Open the Paraview client on your workstation and go to File>Connect. Click on Add Server and set the name to Dardel. Keep the Server Type as Client / Server, the Host as localhost and the Port as 11111. Click on Configure and leave the Startup Type as Manual. Click Save.

## Connect to a remote server on Dardel
Begin by starting the client on your local workstation.
Then login to Dardel using SSH and run the following commands to load the
required modules
```
ml PDC
ml paraview/5.11.1
```
Now allocate an interactive job to run the server in. Depending on the size of the data you may want to use more or less cores, and depending on the task you may want more or less time. This example allocates one node (128 cores) for 60 minutes
```
salloc -n 128 -t 60 -p main -A PROJECT_ID
```
If you do not know your project id, you can find it using the ``projinfo`` command.
Now start the Paraview server using the same number of tasks as you requested in the allocation
```
srun -n 128 pvserver
```
This command will print a few lines of text. There are two important lines to take note of
```
This is nidXXXXXX, your connect-id is YYYY
```
You will need to copy the connect-id into your client in the next step. The other important line is quite long and starts like this
```
ssh -n -L 127.0.0.1:11111:...
```
Copy this whole line, and then open a new terminal window on you local workstation. In this terminal window, paste the SSH command. It will not print anything, but make sure to keep the window open while you are using Paraview. The command opens a tunnel between your workstation and the compute node so that the client and server can communicate securely.
Now, go to the Paraview client on your workstation and navigate to File>Connect. Double-click the Dardel server you added in the previous step. A window will open asking for the connect-id. Use the connect-id printed by the server from the srun command.
If everything goes well, your local client is now connected to a remote Paraview server running on Dardel! You can now open files directly on Klemming and visualize them using Dardel, and view the results on your workstation. If you want to see the remote processors you are connected to, open the Memory Inspector in the View menu.

## Using Paraview
If you are new to using Paraview, there are many resources available online. See for instance the Paraview User's Guide: https://docs.paraview.org/en/v5.11.1/.

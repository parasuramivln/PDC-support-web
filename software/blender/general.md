
# How to use Blender on PDC machines
Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game creation.
For more information see
https://www.blender.org/
To see which versions of blender are installed at PDC, log into the machine and type
module avail blender


## How to use

To see what versions of FDTD Solutions are available on each machine use the command
module avail blender

# Starting the GUI
The GUI can be started using
```
module add blender/2.77a
blender
```
or
```
module add blender/2.77a
blender-softwaregl
```
to start blender without trying to use the GPU to do the rendering

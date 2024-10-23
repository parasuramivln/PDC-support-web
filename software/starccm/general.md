
# How to use StarCCM+ on PDC machines
StarCCM+ is commercial software, and PDC does not have a license. All licenses
to use StarCCM+ at PDC must be supplied by the users.


## How to use

The Star-CCM files can be accessed by loading the appropriate modules. To see which versions of Star-CCM+ are available use the command
module avail starccm+
In order to use StarCCM+ at PDC you must provide your own license for the software.  You can either use the environment variable
CDLMD_LICENSE_FILE
to set to point to the correct license server (not the PoD server 1999@flex.cd-adapco.com), or get access to STAR-CCM+ through license keys generated "power-on-demand" with additional options in the command line
-podkey your_license_key -licpath 1999@flex.cd-adapco.com
where "your_license_key" is the license key.

# Running on the Batch system
sample job script
You can control number of MPI processes by -np option in the execution command
-np 256


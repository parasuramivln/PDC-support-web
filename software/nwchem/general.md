NWChem aims to provide its users with computational chemistry tools that are
scalable both in their ability to treat large scientific computational
chemistry problems efficiently, and in their use of available parallel
computing resources from high-performance parallel supercomputers to
conventional workstation clusters.
For more information see: http://www.nwchem-sw.org


## How to use

Example run script:
Note that this script edits the input template "input_template" and replaces
``<<++SCRDIR++>>`` by the actual scratch directory
```

# scratch_dir <<++SCRDIR++>>
```

## Troubleshooting
A workaround for the error
```
MemRegister in mem_register; err 3
```
is to set
```
export ONESIDED_USE_UDREG=1
```

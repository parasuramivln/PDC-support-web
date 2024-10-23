FastQC is a bioinformatics quality control tool for high throughput sequence data https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

## How to use

You can check which versions of FastQC are available using
```
$ module avail fastqc
```
FastQC has a graphical user interface. It can be run on tegner in an interactive session.
salloc --nodes=1 -t 1:00:00 -A <project>
# Wait for message 'salloc: Granted job allocation <jobid>'
echo $SLURM_NODELIST
# Login to the booked node
ssh -Y <username>@<nodename>.pdc.kth.se
module add fastqc
fastqc&

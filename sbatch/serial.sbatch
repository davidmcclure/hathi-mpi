#!/bin/bash
#
#all commands that start with SBATCH contain commands that are just used by SLURM for scheduling
#################
#set a job name
#SBATCH --job-name=serial
#################
#a file for job output, you can check job progress
#SBATCH --output=serial.out
#################
# a file for errors from the job
#SBATCH --error=serial.err
#################
#time you think you need; default is one hour
#in minutes in this case, hh:mm:ss
#SBATCH --time=01:05:00
#################
#quality of service; think of it as job priority
#SBATCH --qos=normal
#################
#number of nodes you are requesting
#SBATCH --nodes=1
#################
#memory per node; default is 4000 MB per CPU
#SBATCH --mem=4000
#you could use --mem-per-cpu; they mean what we are calling cores
#################
#tasks to run per node; a "task" is usually mapped to a MPI processes.
# for local parallelism (OpenMP or threads), use "--ntasks-per-node=1 --cpus-per-task=16" instead
#SBATCH --ntasks-per-node=1
#################

module load openmpi/1.10.2/gcc
module load python/3.3.2

export PYTHONPATH=/home/dclure/hathi-mpi

$PYTHONPATH/env/bin/python $PYTHONPATH/jobs/serial.py 3600

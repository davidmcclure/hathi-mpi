#!/bin/bash
#
#all commands that start with SBATCH contain commands that are just used by SLURM for scheduling
#################
#set a job name
#SBATCH --job-name=scatter
#################
#a file for job output, you can check job progress
#SBATCH --output=scatter.out
#################
# a file for errors from the job
#SBATCH --error=scatter.err
#################
#time you think you need; default is one hour
#in minutes in this case, hh:mm:ss
#SBATCH --time=3:00:00
#################
#quality of service; think of it as job priority
#SBATCH --qos=normal
#################
#number of nodes you are requesting
#SBATCH --nodes=16
#################
#memory per node; default is 4000 MB per CPU
#SBATCH --mem=64000
#you could use --mem-per-cpu; they mean what we are calling cores
#################
#tasks to run per node; a "task" is usually mapped to a MPI processes.
# for local parallelism (OpenMP or threads), use "--ntasks-per-node=1 --cpus-per-task=16" instead
#SBATCH --ntasks-per-node=16
#################

module load openmpi/1.10.2/gcc
module load python/3.3.2

export PYTHONPATH=/home/dclure/hathi-mpi

mpirun -x PYTHONPATH $PYTHONPATH/env/bin/python \
    $PYTHONPATH/jobs/scatter_list.py

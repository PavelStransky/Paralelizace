#!/bin/bash
#SBATCH --array 1-10
#SBATCH --partition ffa
#SBATCH --mem 500M
#SBATCH --cpus-per-task 10
#SBATCH --job-name=paralelizace
#SBATCH --error=paralelizace.%a.log
#SBATCH --output=paralelizace.%a.log
#SBATCH --open-mode append

# Here, do the real work
# Just a simple example:
python paralelizace.py $SLURM_ARRAY_TASK_ID
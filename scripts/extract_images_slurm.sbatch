#!/bin/bash
##
## extract_images_slurm.sh: run the parallel text_scraper.py script to extract
##      text from a large directory of images
##
## Lines starting with #SBATCH are read by Slurm. Lines starting with ## are comments.
## All other lines are read by the shell.
##
#SBATCH --job-name    extracttextparalell        # job name
#SBATCH --output      extracttextparalell-%j.out # standard output file (%j = jobid)
#SBATCH --error       extracttextparalell-%j.err # standard error file
#SBATCH --partition   classpart      # queue partition to run the job in
#SBATCH --account     classroom
#SBATCH --cpus-per-task=40          # number of CPU cores to allocate
#SBATCH --array       1-36          # do 36 batches of 29 posts
#SBATCH --mem         40000         # 2000 MB of Memory allocated; set --mem with care
#SBATCH --time        0-00:10:00     # Maximum job run time

module load Anaconda3/5.3.0
source activate $HOME/condaenv/
python $HOME/Final/text_scraper_single.py $SLURM_ARRAY_TASK_ID

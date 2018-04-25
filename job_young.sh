#!/bin/bash
#SBATCH -p gpu
#SBATCH -t 0-12:00:00
#SBATCH --job-name=GENDER_AGE
#SBATCH --mem=30GB 
#SBATCH --output=output_%j.txt
#SBATCH -e error_%j.txt
#SBATCH --gres=gpu:2

source activate AGE_GENDER
python guess.py --target age_young.csv --model_type inception --model_dir ./models/age/ --filename image_paths_young.txt --device_id /device:GPU:0 --single_look 
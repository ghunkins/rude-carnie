#!/bin/bash
#SBATCH -p gpu
#SBATCH -t 0-02:00:00
#SBATCH --job-name=GENDER_AGE
#SBATCH --mem=30GB 
#SBATCH --output=output_%j.txt
#SBATCH -e error_%j.txt
#SBATCH --gres=gpu:2

source activate AGE_GENDER
python guess.py --target age.csv --model_type inception --model_dir ./models/age/ --filename image_paths.txt --single_look
python guess.py --target gender.csv --model_type inception --model_dir ./models/gender/ --filename image_paths.txt --single_look --class_type gender
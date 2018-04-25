"""
Join the age.csv and gender.csv.
Rename all files.
"""

import pandas
import os

FOLDER = '/Users/ghunk/Desktop/GRADUATE/CSC_449/Final_Project/face-alignment/extracted/'

GENDER_CSV = '/Users/ghunk/Desktop/GRADUATE/CSC_449/Final_Project/rude-carnie/gender.csv'
AGE_CSV = '/Users/ghunk/Desktop/GRADUATE/CSC_449/Final_Project/rude-carnie/age.csv'

AGE_LIST = ['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
AGE_DICT = {x: x.replace(', ', '-') for x in AGE_LIST}

if __name__ == '__main__':
	age_df = pandas.read_csv(AGE_CSV)
	gender_df = pandas.read_csv(GENDER_CSV)
	age_df['label'] = age_df['label'].apply(lambda x: AGE_DICT[x])
	joined_df = pandas.merge(age_df, gender_df, on=['file'], suffixes=('_age', '_gender'))
	for index, row in joined_df.iterrows():
		file_name = '_'.join([row['label_gender'], row['label_age']]) + '.jpg'
		split = row['file'].split('/')
		orig_file = FOLDER + '/'.join([split[-2], split[-1]])
		new_file = FOLDER + '/'.join([split[-2], file_name])
		print orig_file
		print new_file
		os.system("rm {0}".format(orig_file))
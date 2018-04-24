"""
Remove files that meet a condition
from a glob.
"""
import glob

folder = '/scratch/ghunkins/rude-carnie/extracted/'

if __name__ == '__main__':
	image_list = glob.glob(folder+'**/*.jpg', recursive=True)
	with open('image_paths.txt', 'w') as f:
		for image_path in image_list:
			if not 'origin.jpg' in image_path:
				f.write("{}\n".format(image_path))


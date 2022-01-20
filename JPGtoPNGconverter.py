from PIL import Image
import os
import sys


src_folder = sys.argv[1]
result_folder = sys.argv[2]


if not os.path.exists(result_folder):
	os.mkdir(result_folder)


contents = os.listdir(path= src_folder)

print(contents)

for image in contents:
	im = Image.open(os.path.join(src_folder, image))
	clean_name = os.path.splitext(image)[0]
	o_file = os.path.join(result_folder,f'{clean_name}.png')
	im.save(o_file, 'png')

print('done!')

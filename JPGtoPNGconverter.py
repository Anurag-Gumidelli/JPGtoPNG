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
	print(im)
	loc = image.replace('.jpeg', '.png')
	print(loc)
	o_file = os.path.join(result_folder,''.join(loc))
	print(o_file)
	im.save(o_file)

print('done!')

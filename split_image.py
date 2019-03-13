from PIL import Image
import glob
import sys
import os

# USAGE:
# python <split_image.py> <input_dir> <output_dir>
# where input_dir conatains PNG files (outputs from the model)
# and output_dir will contain 10 PNG files labeled by bucket number


if len(sys.argv) != 3:
    print("WRong args")
    exit(1)

output_dir = sys.argv[2]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_names = glob.glob(sys.argv[1] + "/*.png")
for name in file_names:
    basename = os.path.basename(name)
    im = Image.open(name)
    print("Opened image: {}".format(name))

    for i in range(10):
        x = 148 + (140*i)
        y = 8
        crop_rectangle = (x, y, x+128, y+128)
        cropped_im = im.crop(crop_rectangle)
        cropped_im.save(output_dir + "/Bucket_" + str(i) + "_" + basename)

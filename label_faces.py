import csv
import sys
import glob
import os
from shutil import copyfile

def bmiToBucket(bmi):
    if bmi < 23:
        return 0
    elif bmi < 25:
        return 1
    elif bmi < 27:
        return 2
    elif bmi < 29:
        return 3
    elif bmi < 31:
        return 4
    elif bmi < 33:
        return 5
    elif bmi < 36:
        return 6
    elif bmi < 39:
        return 7
    elif bmi < 44:
        return 8
    else:
        return 9

def genderToBucket(gender):
    if gender == "Male":
        return 0
    else:
        return 1

def getFileNameForImage(base_name, bmi, gender):
    directory = "./labeled/"+str(bmiToBucket(float(bmi)))+"."+str(genderToBucket(gender))+"/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = directory+base_name+".jpg"
    return file_name

# Arg 1: Path to CSV file
file = open(sys.argv[1], "r")
reader = csv.reader(file)

# Image i's label at index i+1
labels = []
for line in reader:
    labels.append(line)

file_names = glob.glob("./unlabeled/" + "*.jpg")
for name in file_names:
    base_name = os.path.basename(name)
    under = base_name.find("_")
    under2 = base_name.find("_", under+1)
    imageId = base_name[under+1:under2]

    label = labels[int(imageId)+1]
    bmi = label[1]
    gender = label[2]
    new_fileName = getFileNameForImage(base_name, bmi, gender)
    copyfile(name, new_fileName)

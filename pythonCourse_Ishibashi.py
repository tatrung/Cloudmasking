#!/home/trung/miniconda3/bin/python
#from PIL import Image
#im1=Image.open("/media/trung/Data/lena.png")
#imBW=im1.convert('1')
#im1.show()
#imBW.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import gdal
import os
import subprocess

#img_sub="/media/trung/Data/ALAV2A073383360/IMG-02-ALAV2A073383360-OORIRFU_000.tif"
#img_plt=mpimg.imread('/media/trung/Data/ALAV2A073383360/IMG-02-ALAV2A073383360-OORIRFU_000.tif')


#=======see path where python is installed
#python -V
#which python3


#=======run gdallocationinfo using subprocess command
#command=["gdallocationinfo", "-wgs84", img_sub, "106.1087", "11.6039" ]
#result = subprocess.run(command,stdout=subprocess.PIPE)


#=======run gdallocationinfo using os.system command
#os.system("gdallocationinfo -wgs84 /media/trung/Data/ALAV2A073383360/IMG-02-ALAV2A073383360-OORIRFU_000.tif 106.1087 11.6039")


#=======list of names defined by a module by dir() function
#content = dir(os)
#print(content)

#========I/O using raw_input() and input()
#str = input("enter your input: ")
#print(str)

#========opening and closing files
fo = open("foo.txt", "wb")
fo.close()

#========reading and writing files
fo.write(string)
fo.read()

#=========file positions
#fo.tell() # tell the current position within the file, the next read or write will occur at that many bytes from the beginning of the file
#fo.seek(offset, from) #method changes the current file position


#=========file operating
#os.remove("fo.txt") 
#os.mkdir("newfile")
#os.chdir("newdirectories")
#os.rmdir("path to file")



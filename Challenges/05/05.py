#!/usr/bin/python
# URL points to image containing this generated EXIF data
# keep in cyberd.oregonctf.org/static/WHOAMI.jpg
import os
ofile=open('05_final.txt','w+')
ofile.write('http://goo.gl/gUwMe4\n')
ofile.close()
s="the key for number five is shirleysidentities"
command='exiftool -ImageDescription="'+s+'" static/WHOAMI.jpg'
command='exiftool -Description="'+s+'" static/WHOAMI.jpg'
os.system(command)

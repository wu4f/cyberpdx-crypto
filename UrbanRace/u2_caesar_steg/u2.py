#!/usr/bin/python
# After blank filled, URL points to image containing this generated
#   EXIF data
# in cyberd.oregonctf.org/static/brownies.jpg
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u2c => challenge no. 2 for urban race
s=c.u2c
command='exiftool -ImageDescription="'+s+'" static/brownies.jpg'
os.system(command)

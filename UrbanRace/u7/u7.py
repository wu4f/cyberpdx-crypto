#!/usr/bin/python
# The only changes are to the image static/getme.jpg
# Update GPS to the location of the thing to find
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u7latdeg => for winner: location of prize for urban race
latdeg=c.u7latdeg
latref=c.u7latref
longdeg=c.u7longdeg
longref=c.u7longref
command='exiftool -exif:gpslatitude='+latdeg+' -exif:gpslatituderef='+latref+' -exif:gpslongitude='+longdeg+' -exif:gpslongituderef='+longref+' static/getme.jpg'
os.system(command)

#!/usr/bin/python
# The only changes are to the image static/concrete.jpg
# Update GPS to the location of the thing to find
# Update the Scytale image shown on the concrete to encode the riddle
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u6c => challenge no. 6 for urban race
s=c.u6c

latdeg=c.u6latdeg
latref=c.u6latref
longdeg=c.u6longdeg
longref=c.u6longref

s=s.replace(' ','')
msg1="73 63 79 74 61 6c 65 20 74 68 69 73"
msg2=s[0::5]+s[1::5]+s[2::5]+s[3::5]+s[4::5]
img = Image.open("static/concrete_orig.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",60)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((30, 30),msg1,font=font, fill=(0,0,0))
draw.text((30, 180),msg2,font=font, fill=(0,0,0))
img.save('static/concrete.jpg')
command='exiftool -ImageDescription="'+s+'" static/concrete.jpg'
os.system(command)
command='exiftool -exif:gpslatitude='+latdeg+' -exif:gpslatituderef='+latref+' -exif:gpslongitude='+longdeg+' -exif:gpslongituderef='+longref+' static/concrete.jpg'
os.system(command)

#!/usr/bin/python
# Static link http://goo.gl/FsFivj is encoded in ASCII HEX
# Points to http://cyberd.oregonctf.org/static/snake.jpg
# Put encoded Scytale message in EXIF of image
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u5c => challenge no. 1 for urban race
s=c.u5c
link="http://goo.gl/FsFivj"

j="".join([str(hex(ord(c))[2:])+" " for c in link])
outfile=open("u5_final.txt","w")
outfile.write(j+"\n")
outfile.close()

s=s.replace(' ','')
f=s[0::7]+s[1::7]+s[2::7]+s[3::7]+s[4::7]+s[5::7]+s[6::7]
command='exiftool -ImageDescription="'+f+'" static/snake.jpg'
os.system(command)

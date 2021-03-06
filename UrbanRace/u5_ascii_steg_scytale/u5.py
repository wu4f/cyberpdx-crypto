#!/usr/bin/python
# Static link https://goo.gl/igJyl0 is encoded in ASCII HEX
# Points to http://crypto.cyberpdx.org/static/snake.jpg
# Put encoded Scytale message in EXIF of image
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u5c => challenge no. 1 for urban race
s=c.u5c
link="https://goo.gl/igJyl0"

j="".join([str(hex(ord(c))[2:])+" " for c in link])
outfile=open("u5_final.txt","w")
outfile.write(j+"\n")
outfile.close()

s=s.replace(' ','')
f=s[0::8]+s[1::8]+s[2::8]+s[3::8]+s[4::8]+s[5::8]+s[6::8]+s[7::8]
command='exiftool -ImageDescription="'+f+'" static/snake.jpg'
os.system(command)

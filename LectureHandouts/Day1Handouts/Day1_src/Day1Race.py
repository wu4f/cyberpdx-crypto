#!/usr/bin/python3
# Static link https://goo.gl/igJyl0 is encoded in ASCII HEX
# Points to http://crypto.cyberpdx.org/static/snake.jpg
# Put encoded Scytale message in EXIF of image
import os, sys

s="Which King said: "
f="Struggle is a never-ending process"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in f)
s = s+m

link="https://goo.gl/"
goog="qSUUHk"
num=[0x2e, 0x15, 0x3a, 0x1F, 0x2B, 0x38]
original=list(map(ord,goog))
subtracted=list(map(lambda x,y: x - y, original, num))
for i in range(len(original)):
    print("Find what binary {0:08b} is in decimal, then add it to what hexadecimal {1:02X} is in decimal.  Finally, take that decimal number and look up its ASCII character.  This is letter number {2} in the 6 missing characters in https://goo.gl/______\n\n\n\n\n\n\n".format(subtracted[i], num[i],i+1))

command='exiftool -ImageDescription="'+s+'" static/mona.jpg'
os.system(command)

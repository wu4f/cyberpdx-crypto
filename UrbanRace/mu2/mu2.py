#!/usr/bin/python
import os, sys
from itertools import cycle
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.mu2c => challenge no. 2 for mini urban race
s=c.mu2c
s1="Use Scytale Period 8"
m1=''.join(hex(ord(n))[2:].ljust(3,' ') for n in s1)

s2="Decode The Word Below And Use Its Opposite Color To Vigenere Decode"
s2=s2.replace(' ','')
m2=s2[0::7]+s2[1::7]+s2[2::7]+s2[3::7]+s2[4::7]+s2[5::7]+s2[6::7]

s3="BLACK"
m3=''.join([ (" {num:08b}".format(num=ord(c))+"\n") for c in s3])

s4="FilltheblankwithMUK"
key='WHITE'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=s4.upper().replace(' ','')
cycledkey=cycle(key)
m4=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(s4)))

m5="http://crypto.cyberpdx.org/static/____.jpg"
ofile=open("mu2_final.txt","w+")
ofile.write(m1+"\n\n"+m2+"\n\n"+m3+"\n\n"+m4+"\n\n"+m5+"\n")
ofile.close()
command='exiftool -ImageDescription="'+s+'" static/MUK.jpg'
os.system(command)
command='exiftool -ImageDescription="'+s+'" static/muk.jpg'
os.system(command)

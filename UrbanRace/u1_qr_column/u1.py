#!/usr/bin/python
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c
import pyqrcode

# c.u1c => challenge no. 1 for urban race

s=c.u1c
colstr="DUTCH"
msg=colstr+s.replace(' ','')
cols=len(colstr)
pad= len(colstr) - (len(msg) % cols)
msg=msg+pad*" "
s=[msg[n:n+cols] for n in range(0,len(msg),cols)]
ps=""
for line in s:
    ps += line[4]+" "+line[2]+" "+line[0]+" "+line[1]+" "+line[3]+"\n"
estring=pyqrcode.create(ps)
estring.svg('u1_final.svg',scale=8)

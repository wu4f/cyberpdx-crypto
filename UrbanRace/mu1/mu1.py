#!/usr/bin/python
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.mu1c => challenge no. 1 for mini urban race

s=c.mu1c
u=open("static/mu1.txt","w+")
u.write(s+"\n")
u.close()

s = "Visit goo.gl with"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in s)
u=open("mu1_final.txt","w+")
u.write(m+"\n\n")
goog="vxFn4j"
binstrurl=''.join([ ("   {num:08b}".format(num=ord(c))+"\n") for c in goog])
u.write(binstrurl+"\n")
u.close()

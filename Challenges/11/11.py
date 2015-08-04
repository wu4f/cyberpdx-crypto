#!/usr/bin/python
s="the key for june seventeenth is surveillance"
t=''.join([ (str(ord(c)) + "\n") for c in s ])
u=open("11.txt","w+")
u.write(t)

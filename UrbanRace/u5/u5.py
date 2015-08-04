#!/usr/bin/python
s=open("u5_plain.txt","r").readlines()
u=open("u5_crypt.txt","w+")
for i in range(0,len(s[0])-1):
    t = ''.join([c[i] for c in s])
    u.write(t)

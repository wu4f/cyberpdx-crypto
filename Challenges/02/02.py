#!/usr/bin/python
s="the key for number two is felinebackdoor"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in s)
u=open("02_final.txt","w+")
u.write(m+"\n")
u.close()

#!/usr/bin/python
s1="the key for number one is:"
s2="catchawave"
t1=''.join([ (str(ord(c))+" ") for c in s1 ])
t2=''.join([ ("   {num:08b}".format(num=ord(c))+"\n") for c in s2 ])
u=open("01_final.txt","w+")
u.write(t1+"\n")
u.write(t2)
u.close()

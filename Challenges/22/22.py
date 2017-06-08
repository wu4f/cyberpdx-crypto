#!/usr/bin/python
colstr="ENGLISH"
#msg=colstr+"thekeyfornumbertwentytwois ringzero"
msg=colstr+"thekeyfornumbertwentytwoisringzero "
cols=len(colstr)
pad= len(colstr) - (len(msg) % cols)
s=[msg[n:n+cols] for n in range(0,len(msg),cols)]
t=open("22_final.txt","w+")
for line in s:
    permute = line[0]+line[2]+line[6]+line[4]+line[3]+line[1]+line[5]
    decstr = ''.join([(" " + str(ord(c)).rjust(3)) for c in permute])
    t.write(decstr+"\n")

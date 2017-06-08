#!/usr/bin/python
s="the key for number six is onionroute"
colstr="FRENCH"
msg=colstr+s.replace(' ','')
cols=len(colstr)
pad= len(colstr) - (len(msg) % cols)
msg=msg+pad*" "
s=[msg[n:n+cols] for n in range(0,len(msg),cols)]
u=open("06_final.txt","w+")
for line in s:
    permute = line[5]+" "+line[3]+" "+line[2]+" "+line[1]+" "+line[0]+" "+line[4]
    u.write(permute+"\n")
u.close()

#!/usr/bin/python
s=open("22_puzzle.txt","r").readlines()
t=open("22.txt","w+")
u=open("22_ascii.txt","w+")
for line in s:
    permute = line[0]+line[2]+line[6]+line[4]+line[3]+line[1]+line[5]
    decstr = ''.join([(" " + str(ord(c)).rjust(3)) for c in permute])
    u.write(permute+"\n")
    t.write(decstr+"\n")

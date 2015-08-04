#!/usr/bin/python
s=open("u4_puzzle.txt","r").readlines()
u=open("u4_ascii.txt","w+")
for line in s:
    permute = line[0]+line[3]+line[4]+line[2]+line[1]
    decstr = ''.join([(" " + str(ord(c)).rjust(3)) for c in permute])
    u.write(permute+"\n")

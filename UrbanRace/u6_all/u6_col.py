#!/usr/bin/python
s=open("u6_column_plain.txt","r").readlines()
u=open("u6_column_ciph.txt","w+")
for line in s:
    permute = line[0]+line[3]+line[4]+line[2]+line[1]
    u.write(permute+"\n")

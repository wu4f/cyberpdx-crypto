#!/usr/bin/python
s="http://goo.gl/FsFivj"
j="".join([str(hex(ord(c))[2:])+" " for c in s])
print j

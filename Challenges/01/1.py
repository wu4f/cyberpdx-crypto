#!/usr/bin/python
s="the key for june seventh is keylogging"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in s)
print m

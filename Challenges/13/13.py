#!/usr/bin/python
# Not self-contained.  Relies on previously generated QR and Barcodes
#   that are static (update metadata in static 2D barcode closer.jpg)
# QR code points to image containing this generated EXIF data
# keep in crypto.cyberpdx.org/static/closer.jpg
#
import os
import pyqrcode
s="the key for number thirteen is firstcatch"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in s).rstrip()
command='exiftool -ImageDescription="'+m+'" static/closer.jpg'
os.system(command)
s='http://crypto.cyberpdx.org/static/closer.jpg'
estring=pyqrcode.create(s)
estring.svg('13_final.svg',scale=8)

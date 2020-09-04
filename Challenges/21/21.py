# Old QR code goes to goo.gl URL that points to a Google Doc that
#   has ASCII HEX for another goo.gl URL
# QR code here replaces this with a goo.gl URL that points to static/url.txt
#   with the same ASCII HEX for another goo.gl URL
# Second goo.gl URL goes to static/tables.jpg image
# Image has info in metadata pointing to static/scytale.txt
# This script generates alternate QR code and modifies scytale.txt with
#   message (It reuses all other initial files)
#
import pyqrcode, os
qr_url="https://goo.gl/OpQU25"
s="the key for number twenty one is dropbobby"
estring=pyqrcode.create(qr_url)
estring.svg('21_final.svg',scale=8)
s=s.replace(' ','')
f=s[0::5]+s[1::5]+s[2::5]+s[3::5]+s[4::5]
outfile=open("static/scytale.txt","w")
outfile.write(f+"\n")
outfile.close()
hex_url="https://goo.gl/bux7yl"
m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in hex_url)
u=open("static/url.txt","w+")
u.write(m+"\n")
u.close()
s="Try this URL instead: http://crypto.cyberpdx.org/static/scytale.txt"
command='exiftool -ImageDescription="'+s+'" static/tables.jpg'
command='exiftool -Description="'+s+'" static/tables.jpg'
os.system(command)

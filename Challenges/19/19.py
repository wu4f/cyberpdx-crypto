#!/usr/bin/python
# Create substitution cipher using s and scramble permutation
# Encode first three words in a barcode
# Encode next two words in a QR code
# Encode last two words in ASCII Hex
import code128
import os
import pyqrcode

s="the key for number nineteen is humanhorse"
alphabet="abcdefghijklmnopqrstuvwxyz "
scramble="czxkpytafnuvdhljmioqwbregs "
sub_dict=dict(zip(alphabet,scramble))
cipherlist=[sub_dict[c] for c in s]
ciphertext=''.join(str(c) for c in cipherlist)
words=ciphertext.split()

barcodestr=words[0]+" "+words[1]+" "+words[2]
qrcodestr=words[3]+" "+words[4]
asciistr=words[5]+" "+words[6]

with open("19a_final.svg", "w") as f:
    f.write(code128.svg(barcodestr))
    f.close()

estring=pyqrcode.create(qrcodestr)
estring.svg('19b_final.svg',scale=8)

m=''.join(hex(ord(n))[2:].ljust(3,' ') for n in asciistr)
with open("19c_final.txt","w") as f:
    f.write(m+"\n")
    f.close()

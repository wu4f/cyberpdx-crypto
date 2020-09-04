#!/usr/bin/python
# Pre-made Goo.gl URL that points to pre-made image containing Hex ASCII
#   that says, "The key can be found here, somewhere" (somewhere.jpg)
# ASCII points students to look into its metadata
# Script generates metadata for image that contains a Vigenere code with
#   given key that decodes a message telling students to use Enigma on a
#   certain day to decode other string
# Other string uses Enigma keys on that day to encode final string
import os
from itertools import cycle
from enigma.machine import EnigmaMachine
s="the key for number twenty is rapidseven in lowercase"
key='EXPLOIT'
descstr="Use "+key+" to decode: "
url="goo.gl/qfNWSH"
binstrurl=''.join([ (" {num:08b}".format(num=ord(c))+"\n") for c in url])
ofile=open("20_final.txt","w+")
ofile.write(binstrurl)
ofile.close()

command='exiftool -Artist="Monsieur Vigenere and Herr Enigma" static/somewhere.jpg'
os.system(command)
vs='Try day twenty'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=vs.upper().replace(' ','')
cycledkey=cycle(key)
ciphertext=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(plaintext)))
descstr+=ciphertext+"\n"

machine = EnigmaMachine.from_key_sheet(
       rotors='IV V VI',
       reflector='B',
       ring_settings='U Y D',
       plugboard_settings='AP BF CK GT HS IM JV NZ RQ WX')

machine.set_display('TOW')
enigma_plaintext = s.upper().replace(' ','')
enigma_ciphertext = machine.process_text(enigma_plaintext)
i=0
enigma_str=""
while i<len(enigma_ciphertext):
    enigma_str += enigma_ciphertext[i:i+4]+" "
    i+=4
descstr+="Then decode:  "+enigma_str
command='exiftool -ImageDescription="'+descstr+'" static/somewhere.jpg'
os.system(command)

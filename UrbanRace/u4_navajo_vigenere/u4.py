# This script encodes vign(msg,ENGINEER) where
#    msg = 'for key four find what was built for joyce near the clocks at the urban center plaza'
from itertools import cycle
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# Navajo code for 'DISPLAY MESSAGE WITH ENGINEER AS SECRET'
navajo_code = "BE-SEIS-NA-NEH HANE-AL-NEH BILH DAY-DIL-JAH-HE ACHE BAH-HAS-TKIH"
#navajo_code = "CHA-GEE BAH-HAS-TKIH YIL-TAS TOH-NI-TKAL-LO CHA-GEE HANE-AL-NEH SEIS DAY-DIL-JAH-HE"

# c.u4c => challenge no. 4 for urban race

s=c.u4c
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=s.upper().replace(' ','')
key='ENGINEER'
cycledkey=cycle(key)
ciphertext=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(plaintext)))
f=open('u4a_final.txt','w')
f.write(navajo_code+"\n\n\n")
f.write('Vigenere key =  ???\n\n')
f.write(ciphertext+"\n")
f.close()

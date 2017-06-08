import barcode
import os
from itertools import cycle

s='the key for number twelve is shinymetal in lowercase'

import code128
with open("12a_final.svg", "w") as f:
    f.write(code128.svg("key=WOODEN"))
    f.close()

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string=s.upper().replace(' ','')
plaintext=string.upper().replace(' ','')
key='WOODEN'
cycledkey=cycle(key)
ciphertext=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(plaintext)))
f=open('12b_final.txt','w')
f.write(ciphertext+"\n")
f.close()

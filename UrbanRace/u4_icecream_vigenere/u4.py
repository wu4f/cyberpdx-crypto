# Ice cream truck encodes: JEANINE
#    Go into Puzzle/C4, run the appropriate scripts to get SVG files
# This script encodes vign(msg,JEANINE) where
#    msg = 'for key four find what was built for joyce near the clocks at the urban center plaza'
from itertools import cycle
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u4c => challenge no. 4 for urban race

s=c.u4c
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=s.upper().replace(' ','')
key='JEANINE'
cycledkey=cycle(key)
ciphertext=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(plaintext)))
f=open('u4a_final.txt','w')
f.write(ciphertext+"\n")
f.close()

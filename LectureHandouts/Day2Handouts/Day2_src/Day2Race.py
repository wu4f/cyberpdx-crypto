import os
from itertools import cycle

sarray=['atreenextto', 'kingalbertis', 'namedaftera', 'galwhoselast', 'nameisschmidt', 'findhername']

karray=['john', 'ben', 'george', 'thomas', 'james', 'pat']

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

c = []
for i in range(len(sarray)):
    key = karray[i]
    thestr = sarray[i].upper()
    cycledkey=cycle(key.upper())
    newstr=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(thestr[i])) % 26] for i in range(len(thestr)))
    c.append(newstr)

colstr = 'CYBER'
col = []
for i in range(len(sarray)):
    s = 'the key for vigenere '+ str(i+1) + ' is '+karray[i].upper()
    msg = colstr+s.replace(' ','')
    cols = len(colstr)
    pad = len(colstr) - (len(msg) % cols)
    msg = msg+pad*" "
    s = [msg[n:n+cols] for n in range(0,len(msg),cols)]
    for line in s:
        permute = line[3]+" "+line[1]+" "+line[2]+" "+line[0]+" "+line[4]
        print(permute)
    print("\nVigenere Message Part #{}: {}\n".format(i+1,c[i]))

#f=open('12b_final.txt','w')
#f.write(ciphertext+"\n")
#f.close()

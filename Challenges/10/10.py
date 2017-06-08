from itertools import cycle
s='the key for number ten is greatwhitecable in lowercase'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=s.upper().replace(' ','')
key='CYBERDIS'
cycledkey=cycle(key)
ciphertext=''.join(alpha[(alpha.index(next(cycledkey))+alpha.index(plaintext[i])) % 26] for i in range(len(plaintext)))
f=open('10_final.txt','w')
f.write("Vigenere Key = " + key + "\n\n")
f.write(ciphertext+"\n")
f.close()

s="the key for number nine is merriamsintrusion"
alphabet="abcdefghijklmnopqrstuvwxyz "
scramble="gxuhiowfbcvprqsnzkeldjatmy "
sub_dict=dict(zip(alphabet,scramble))
cipherlist=[sub_dict[c] for c in s]
ciphertext=''.join(str(c) for c in cipherlist)
f=open('09_final.txt','w')
f.write("You should know how it begins by now....\n\n")
f.write(ciphertext+"\n")
f.close()

# Generated via this code
# foo=list(alphabet)
# shuffle(foo)
# scramble=''.join(foo)

s="the key for number seventeen is reverselook"
alphabet='abcdefghijklmnopqrstuvwxyz '
scramble='tspeockyxwhjizfavunqrgmbld '
outfile=open('17_final.txt','w')
mapping = dict(zip(alphabet,scramble))
message="You know how it should go!"
msg = [hex(ord(c)) for c in message]
outputstr = ''.join(str(c)[2:]+' ' for c in msg)
outfile.write(outputstr+"\n\n")

encrypt_chars = [ mapping[i] for i in s ]
enc=''.join(encrypt_chars)
#print(enc)
msg = [hex(ord(c)) for c in enc]
outputstr = ''.join(str(c)[2:]+' ' for c in msg)
outfile.write(outputstr+"\n")
outfile.close()

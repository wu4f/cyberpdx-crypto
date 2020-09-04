s="the key for number seven is atubertoolbox"
s=s.replace(' ','')
f=s[0::7]+s[1::7]+s[2::7]+s[3::7]+s[4::7]+s[5::7]+s[6::7]
open('07_final.txt','w').write(f+"\n")

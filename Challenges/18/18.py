import pyqrcode
s="the key for number eighteen is perimeterbarrier"
s=s.replace(' ','')
f=s[0::7]+s[1::7]+s[2::7]+s[3::7]+s[4::7]+s[5::7]+s[6::7]
msg='Ever get that feeling of deja vu?\n\n'+f+'\n'
estring=pyqrcode.create(msg)
estring.svg('18_final.svg',scale=8)

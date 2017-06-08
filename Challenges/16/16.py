# Combo Outer-Inner Caesar wheel
# 1. Rotate and translate into both wingdings and symbol
# 2. Copy and paste both translations into Windows PPT file, load in a Windows
#      VM then change to Wingdings/Symbol
# 3. Cut and paste every other word
# 4. Do slideshow and take screenshot via VirtualBox and save image
# 5. Crop in gimp
# 6. Make sure the password and "lowercase" are in Dingbats or
#      ensure the "l" is in non-symbol, non-dingbat font

s="the key for number sixteen is muttonroast in lowercase"
outfile=open('16_ForWindows.txt','w')
alphabet='abcdefghijklmnopqrstuvwxyz '
scramble1='368)[AJNRSTUWXYZzxvuplih>d '
mapping1 = dict(zip(alphabet,scramble1))
encrypt_chars = [ mapping1[i] for i in s ]
enc=''.join(encrypt_chars)
outfile.write(enc+"\n\n")
scramble2='zabxdejghijklmnwpqrstuvwcu '
mapping2 = dict(zip(alphabet,scramble2))
encrypt_chars = [ mapping2[i] for i in s ]
enc=''.join(encrypt_chars)
outfile.write(enc+"\n")
outfile.close()

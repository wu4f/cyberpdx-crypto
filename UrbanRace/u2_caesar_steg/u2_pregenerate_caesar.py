# Combo Outer-Inner Caesar wheel
# Will pre-generate message that fills in the blank on the URL given
# Run u2.py to update level with a Steg that has message for key two
#
# 1. Rotate and translate into both wingdings and symbol
# 2. Copy and paste both translations into Windows PPT file, load in a Windows
#      VM then change to Wingdings/Symbol
# 3. Cut and paste every other word
# 4. Do slideshow and take screenshot via VirtualBox and save image
# 5. Crop in gimp
s="fill in the blank with brownies in lowercase"
outfile=open('u2a_ForWindows.txt','w')
outfile.write(s+"\n\n")
alphabet='abcdefghijklmnopqrstuvwxyz '
scramble1='zxvuplih>d368)[AJNRSTUWXYZ '
mapping1 = dict(zip(alphabet,scramble1))
encrypt_chars = [ mapping1[i] for i in s ]
enc=''.join(encrypt_chars)
outfile.write(enc+"\n\n")
scramble2='uzabxdejghijklmnwpqrstuvwc '
mapping2 = dict(zip(alphabet,scramble2))
encrypt_chars = [ mapping2[i] for i in s ]
enc=''.join(encrypt_chars)
outfile.write(enc+"\n")
outfile.close()

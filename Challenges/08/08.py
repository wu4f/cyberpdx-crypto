# Outer Caesar wheel
# 1. Rotate and translate into wingdings
# 2. Copy and paste characters into Windows PPT file, load in a Windows
#      VM then change to Wingdings
# 3. Do slideshow and take screenshot via VirtualBox and save image
# 4. Crop in gimp
s="the key for number eight is codepattern in lowercase"
alphabet='abcdefghijklmnopqrstuvwxyz '
scramble='UWXYZzxvuplih>d368)[AJNRST '

mapping = dict(zip(alphabet,scramble))

encrypt_chars = [ mapping[i] for i in s ]
enc=''.join(encrypt_chars)
open('08_ForWindows.txt','w').write(enc+"\n")

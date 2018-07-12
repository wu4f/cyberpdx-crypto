#!/usr/bin/python
# Create a column transposition of URL that points to Caesar image et_tu.jpg
#
# Outer Caesar wheel
# 1. Rotate and translate into wingdings
# 2. Copy and paste characters into Windows PPT file, load in a Windows
#      VM then change to Wingdings
# 3. Save textbox as a JPEG picture and bring back as static/et_tu.jpg

s="the key for number fifteen is mousetakeover in lowercase"
colstr="POLISH"
# old url with confusing characters
#msg=colstr+"theurlthatyouwanttotryishttps://goo.gl/rO1yRx"
msg=colstr+"theurlthatyouwanttotryishttps://goo.gl/Njpsct"
cols=len(colstr)
pad= len(colstr) - (len(msg) % cols)
msg=msg+pad*" "
t=[msg[n:n+cols] for n in range(0,len(msg),cols)]
u=open("15_final.txt","w+")
for line in t:
    permute = line[5]+" "+line[3]+" "+line[2]+" "+line[1]+" "+line[0]+" "+line[4]
    u.write(permute+"\n")

alphabet='abcdefghijklmnopqrstuvwxyz '
scramble='ih>d368)[AJNRSTUWXYZzxvupl '

mapping = dict(zip(alphabet,scramble))

encrypt_chars = [ mapping[i] for i in s ]
enc=''.join(encrypt_chars)
open('15_ForWindows.txt','w').write(enc+"\n")

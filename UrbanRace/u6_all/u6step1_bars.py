#!/usr/bin/python
# 3 parts of initial puzzle lead you to two barcodes that spell out
#  decimal ASCII for getting you to goo.gl URL pointing to
#  ccvqr.png
import code128, sys, os
from PIL import Image

txt1="goo.gl/"
# old txt2 = nH7ohB
txt2="xsLmTU"
t1=''.join([ (str(ord(c))+" ") for c in txt1 ])
t2=''.join([ (str(ord(c))+" ") for c in txt2 ])

code128.image(t1).save("u6_b1.png")
code128.image(t2).save("u6_b2.png")

image1 = Image.open('u6_b1.png')
image2 = Image.open('u6_b2.png')

maxwidth = max(image1.size[0],image2.size[0])
new_im = Image.new(mode='RGB',size=(maxwidth,20+image1.size[1]+image2.size[1]),color=(255,255,255))

y_offset = image1.size[1] + 20

new_im.paste(image1,(0,0))
new_im.paste(image2,(0,y_offset))
new_im.save('static/bars.jpg')
os.system("rm u6_b1.png u6_b2.png")

import pyqrcode
s='http://crypto.cyberpdx.org/static/ccv.jpg'
estring=pyqrcode.create(s)
estring.png('static/ccvqr.png',scale=10)
#estring.png('static/04_final.svg',scale=8)

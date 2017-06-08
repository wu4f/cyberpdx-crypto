import pyqrcode
s='the key for number four is perceiveyourgoal'
estring=pyqrcode.create(s)
estring.svg('04_final.svg',scale=8)

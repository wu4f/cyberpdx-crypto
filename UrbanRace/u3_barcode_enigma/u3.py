from enigma.machine import EnigmaMachine
# setup machine according to specs from a daily key sheet:
import code128
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

# c.u3c => challenge no. 3 for urban race
s=c.u3c

with open("u3a_final.svg", "w") as f:
    f.write(code128.svg("Today is 0x22"))
    f.close()

machine = EnigmaMachine.from_key_sheet(
       rotors='VII I II',
       reflector='C',
       ring_settings='F T P',
       plugboard_settings='AX EC GB KU PH SO TD VQ WR ZM')

# set machine initial starting position
machine.set_display('ZWQ')

plaintext = s.upper().replace(' ','')
ciphertext = machine.process_text(plaintext)
f=open('u3b_final.txt','w')
i=0
while i<len(ciphertext):
    f.write(ciphertext[i:i+4]+" ")
    i+=4
f.write("\n")
f.close()

# 2015
#   day.refl.wheels.ring.grnd.plugs
#   16.B.VIII I II.SBE.GZU.BT CH GV IK LS MU NY QR WE ZA
#   the key for june sixteenth is webster in lowercase
#   IAFZ QWBI AICT TITC AYVO GFXC BBPV QMJA QJBU SFUR FP

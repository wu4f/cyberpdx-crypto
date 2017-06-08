from enigma.machine import EnigmaMachine
s="the key for number fourteen is hailmary in lowercase"
scy="the key can be found using enigma on day fourteen."
scy=scy.replace(' ','')
f=scy[0::6]+scy[1::6]+scy[2::6]+scy[3::6]+scy[4::6]+scy[5::6]
outfile=open('14_final.txt','w')
outfile.write(f+"\n\n")

# setup machine according to specs from a daily key sheet:
machine = EnigmaMachine.from_key_sheet(
       rotors='VIII IV VI',
       reflector='B',
       ring_settings='F X S',
       plugboard_settings='BP CS EZ HY LD OK QJ TW UR XM')

# set machine initial starting position
machine.set_display('UZN')

plaintext = s.upper().replace(' ','')
ciphertext = machine.process_text(plaintext)
i=0
while i<len(ciphertext):
    outfile.write(ciphertext[i:i+4]+" ")
    i+=4
outfile.write("\n")
outfile.close()

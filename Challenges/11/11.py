from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:

s="the key for number eleven is greeksubterfuge in lowercase"
machine = EnigmaMachine.from_key_sheet(
       rotors='VIII I II',
       reflector='B',
       ring_settings='S B E',
       plugboard_settings='BT CH GV IK LS MU NY QR WE ZA')

# set machine initial starting position
machine.set_display('GZU')

plaintext = s.upper().replace(' ','')
ciphertext = machine.process_text(plaintext)
f=open('11_final.txt','w')
f.write("Without the spiritual world the material world is a\n disheartening ______.  Joseph Joubert (1754-1824)\n\n")
f.write("Try Day 0xB\n ")
i=0
while i<len(ciphertext):
    f.write(ciphertext[i:i+4]+" ")
    i+=4
f.write("\n")
f.close()

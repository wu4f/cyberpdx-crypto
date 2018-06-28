def scytale_it(s,n):
    s=s.replace(' ','')
    print("length: ",len(s)," mod: ",n)
    print(''.join(s[i::n] for i in range(0,n)))
    #f=s[0::5]+s[1::5]+s[2::5]+s[3::5]+s[4::5]
    #return f

print(scytale_it("education without",4))
print(scytale_it("morals is like",4))
print(scytale_it("a ship without",4))
print(scytale_it("a compass, merely",5))
print(scytale_it("wandering nowhere",4))
print(scytale_it("martin luther king jr",6))

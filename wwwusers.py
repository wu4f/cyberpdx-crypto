import json
try:
    usersfile=open("users","r")
    d = dict([line.split() for line in usersfile])
    usersfile.close()
except:
    print("Error opening users file")
    exit()

with open("www_paste_users_into_login.py","w") as pyusers:
    pyusers.write("users = {\n")
    for u in d: 
        pyusers.write('''    '{}': ['{}', '{}'],\n'''.format(u,d[u],u))
    pyusers.write("}\n")
    pyusers.close()

import code128

with open("03a_final.svg", "w") as f:
    f.write(code128.svg("the key for number"))
    f.close()

with open("03b_final.svg", "w") as f:
    f.write(code128.svg("three is thepigsays"))
    f.close()

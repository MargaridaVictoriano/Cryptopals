def fixedxor():
    s0 = "1c0111001f010100061a024b53535009181c".decode("hex")
    s1 = "686974207468652062756c6c277320657965".decode("hex")
    string = "".join(chr(ord(s0[i]) ^ ord(s1[i])) for i in range(0,len(s0)))
    print string.encode("hex")

fixedxor()

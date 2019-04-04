def singlebytexortry():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")
    for i in range(0,256):
        st = "".join(chr(ord(s[k])^i) for k in range(0,len(s)))
        print st
singlebytexortry()

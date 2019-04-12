def repeatingKeyXOR(s,key):
  finalKey = key
  while len(finalKey) < len(s):
    finalKey += key
  out = "".join(chr(ord(s[i])^ord(finalKey[i])) for i in range(0, len(s)))
  print out.encode("hex")

def main():
  s = raw_input(" > Plaintext: ")
  k = raw_input(" > Key:  ")
  repeatingKeyXOR(s,k)
main()

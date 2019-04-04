freqs = {
    'A': 0.0651738,
    'B': 0.0124248,
    'C': 0.0217339,
    'D': 0.0349835,
    'E': 0.1041442,
    'F': 0.0197881,
    'G': 0.0158610,
    'H': 0.0492888,
    'I': 0.0558094,
    'J': 0.0009033,
    'K': 0.0050529,
    'L': 0.0331490,
    'M': 0.0202124,
    'N': 0.0564513,
    'O': 0.0596302,
    'P': 0.0137645,
    'Q': 0.0008606,
    'R': 0.0497563,
    'S': 0.0515760,
    'T': 0.0729357,
    'U': 0.0225134,
    'V': 0.0082903,
    'W': 0.0171272,
    'X': 0.0013692,
    'Y': 0.0145984,
    'Z': 0.0007836,
    ' ': 0.1918182
}
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
valid_l = letters + letters.lower() + " "
def score(s):
    score = 0
    for i in s:
        if i in valid_l:
            c = i.upper()
            if c in freqs:
				score += freqs[c]
    return score


def main():
	with open("ch4.txt", "r") as file:
		flag = 0
		for lines in file:
			line = lines[:-1].decode("hex")
			if flag == 0:
				final = "".join(chr(ord(line[j])^0) for j in range(0,len(line)))
				maxScore = score(final)
				flag = 1
			for i in range(1,256):
				current = "".join(chr(ord(line[j])^i) for j in range(0,len(line)))
				currentScore = score(current)
				if currentScore > maxScore:
					maxScore = currentScore
					final = current
	print ">> Case with highest score : " + final
main()

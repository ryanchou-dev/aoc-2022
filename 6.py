import sys

sys.stdin = open("inp.txt", "r")

s = input()
s ='a'+s

for i in range(15, len(s)):
	# substring of length 4
	sub = s[i-14:i]
	if(i==15): print(sub)

	z = set()
	for j in sub: z.add(j)

	if (len(z) == 14): 
		print(i-1)
		exit()
import sys

sys.stdin = open("inp.txt", "r")

e = [0 for i in range(1000)]
x = 1
waitwhat = 2
for i in range(1,146):
	s = input().split()
	if (s[0] == 'addx'):

		e[i+waitwhat] += int(s[1])
		waitwhat += 1
	else:
		pass

e[1]=1
for i in range(2,1000): e[i]+=e[i-1]

px = 1
for i in range(6):
	for j in range(40):
		if (abs(j-e[px]) <= 1):
			print("#", end = "")
		else: print(" ", end = "")
		px += 1
	print()
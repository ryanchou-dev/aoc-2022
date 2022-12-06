import sys

sys.stdin = open("inp.txt", "r")

xs = []
cr = 0
for i in range(2243):

	x = input()
	if (x != ""):
		cr += int(x)
	else:
		xs.append(cr)
		cr = 0
xs.sort()

print(xs[-1]+xs[-2]+xs[-3])

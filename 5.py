import sys

sys.stdin = open('inp.txt', 'r')


x = [[] for i in range(9)]

for i in range(8):
	s = input()

	z = 0
	for i in range(0, len(s), 4):
		if (s[i] == '['):
			x[z].append(s[i+1])
		z+=1

input()
input()
for i in range(503):
	s = input()
	s = s.split()

	num = int(s[1])
	fromm = int(s[3])
	too = int(s[5])


	fromm -= 1
	too -= 1
	print(fromm, too)
	print(x[fromm], x[too])


	x[too] = [z for w in [x[fromm][:num], x[too]] for z in w]
	for j in range(num):
		x[fromm].pop(0)
	print(x[fromm], x[too])


for i in range(9):
	if (len(x[i]) == 0): continue
	print(x[i][0], end="")
print()


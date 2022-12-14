import sys
sys.stdin = open("inp.txt", "r")


weee = [[0 for i in range(10000)] for j in range(10000)]
fl = 0
for i in range(146):
	s = input().split(' -> ')

	prv = list(map(int, s[0].split(',')))
	fl = max(fl, prv[1])

	for j in s[1:]:
		cr = list(map(int, j.split(',')))
		fl = max(fl, cr[1])
		if (cr[0] == prv[0]):
			for k in range(prv[1], cr[1] + 1):
				# print(prv[0],k)
				weee[prv[0]][k] = 1
			for k in range(cr[1], prv[1] + 1):
				# print(prv[0],k)
				weee[prv[0]][k] = 1
		else:
			for k in range(prv[0], cr[0] + 1):
				# print(k,prv[1])
				weee[k][prv[1]] = 1 
			for k in range(cr[0], prv[0]+1):
				# print(k,prv[1])
				weee[k][prv[1]] = 1 
		prv = cr

for j in range(10000):
	weee[j][fl + 2] = 1
print(fl+2)

# for i in range(494,504):
	# for j in range(10):
		# print(weee[i][j], end='')
	# print()
# print(weee[494:504][0:10])

for i in range(50000):
	pos = [500,0]
	if (weee[pos[0]][pos[1]] == 1):
		print(i)
		break
	flg=0
	for j in range(50000):
		if (weee[pos[0]][pos[1]+1] == 0):
			pos[1] += 1
		elif weee[pos[0]-1][pos[1]+1] == 0:
			pos[0]-=1
			pos[1]+=1
		elif weee[pos[0]+1][pos[1]+1] == 0:
			pos[0]+=1
			pos[1]+=1
		else:
			print(pos[0],pos[1])
			weee[pos[0]][pos[1]] = 1
			break


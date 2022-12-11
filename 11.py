from copy import deepcopy
import sys
import math
sys.stdin = open("inp.txt", "r")

x = []
for _ in range(8):
	input()
	zed = []
	strt = input().split(',')
	for j in range(len(strt)):
		if j == 0:
			# print(strt[j].split())
			zed.append(int(strt[j].split()[2]))
		else:
			zed.append(int(strt[j]))
	
	ops = input().split('=')
	ree = ops[1].split()

	key = []
	key.append(zed)
	key.append(ree)

	tst = int(input().split()[-1])
	key.append(tst)
	good = int(input()[-1])
	bad = int(input()[-1])
	key.append(good)
	key.append(bad)
	x.append(key)

	input()


# i don't think product gets that big actually
lcm = 1
for i in range(8):
	lcm = (lcm * x[i][-3]) // math.gcd(lcm, x[i][-3])


ans = [0 for _ in range(8)] 
for i in range(10000):
	
	
	for j in range(8):
		for k in range(len(x[j][0])):
			ans[j] += 1

			ree = deepcopy(x[j][1])
			for l in range(len(ree)):
				if (ree[l] == 'old'): ree[l] = x[j][0][k]
				ree[l] = str(ree[l])


			equa =0
			exec("equa=" + ''.join(ree))

			equa %= lcm
			# equa//=3
			if equa % x[j][2] == 0:
				x[x[j][3]][0].append(equa)
			else:
				x[x[j][4]][0].append(equa)
		x[j][0] = []


ans.sort()
print(ans)
print(ans[-1] * ans[-2])






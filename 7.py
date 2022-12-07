import sys
from collections import defaultdict

sys.stdin = open("inp.txt", "r")

input()
cdir = "/"

dictt = defaultdict(list)

for i in range(1, 1010):
	s = input().split()
	if s[0] == '$':
		if (s[1] == 'ls'): continue
		if s[2] == '..': cdir = '/'.join(cdir.split('/')[:-2]) + '/'
		elif s[2] == '/': cdir = '/'
		else: cdir += s[2] + '/'
	else:
		x=s
		if x[0] == 'dir':
			pass
		else:
			ccdir = '/'
			jj = cdir.split('/')
			dictt['/'].append(int(x[0]))
			for j in jj:
				if (j == ''): continue
				ccdir += j + '/'
				dictt[ccdir].append(int(x[0]))

		

		
ans = 10000000000
vval = 30000000 - (70000000 - sum(dictt['/']))
print("REE", vval)

for k, v in dictt.items():
	sm = 0
	for i in v:
		sm += i
	print(sm, k)
	if sm >= vval:
		ans = min(ans, sm)
print(ans)
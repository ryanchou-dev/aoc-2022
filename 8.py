import sys
from collections import defaultdict

sys.stdin = open("inp.txt", "r")

v = [[0] * 100 for i in range(100)]
for i in range(99):
	s = input()
	for j in range(99):
		v[i][j] = int(s[j])
ans = 0
for i in range(99):
	for j in range(99):

		cur = 0
		zans = 1
		
		for k in range(j + 1, 99):
			cur += 1
			if v[i][k] >= v[i][j]:
				ok = 0
				break

		zans *= cur;
		cur=0
		
		for k in range(j -1, -1, -1):
			cur += 1
			if v[i][k] >= v[i][j]:
				ok = 0
				break

		zans *= cur;
		cur=0
		
		# up
		for k in range(i + 1, 99):
			cur += 1
			if v[k][j] >= v[i][j]:
				break

		zans *= cur;
		cur=0
		
		ok = 1
		# right
		for k in range(i - 1, -1, -1):
			cur += 1
			if v[k][j] >= v[i][j]:
				break
		zans *= cur
		cur = 1
		if (zans == 994): print(i,j)
		ans = max(ans, zans)

print(ans)
		
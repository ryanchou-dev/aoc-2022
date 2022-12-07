import sys

sys.stdin = open("inp.txt", "r")
ans = 0
for _ in range(1000):
	s = input().split(',')
	l = s[0].split('-')
	r = s[1].split('-')
	ok = 0
	for i in range(int(l[0]), int(l[1])+1):
		for j in range(int(r[0]), int(r[1])+1):
			if (i==j):ok=1
	ans += ok
print(ans)
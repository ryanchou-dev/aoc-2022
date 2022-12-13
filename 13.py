import sys
import json
from functools import cmp_to_key
sys.stdin = open("inp.txt", "r")
sys.setrecursionlimit(0x100000)

ind = 1

def rec(x, y):
	if type(x) == int and type(y) == int:
		if x < y:
			return -1
		elif x > y:
			return 1
		return 0
	
	else:
		if type(x) != list: x = [x]
		if (type(y) != list): y = [y]

		pt = 0
		rpt = 0
		while (True):
			if pt >= len(x) and rpt >= len(y): return 0
			if pt >= len(x): return -1
			elif rpt >= len(y): return 1
			rettt = rec(x[pt], y[rpt])
			if rettt == -1:
				return -1
			elif rettt == 1:
				return 1
			else: pass
			
			pt += 1
			rpt += 1

		

ans = 0
reee = []
while True:
	try:
		f = input()
		s = input()

		f = json.loads(f)
		s = json.loads(s)
		reee.append([f])
		reee.append([s])


		if rec(f, s) == -1:
			ans += ind

		ind += 1

		input()
	except EOFError:
		print(ans)
		break

reee.append([[2]])
reee.append([[6]])
reee.sort(key=cmp_to_key(rec))
ff = reee.index([[2]])
ss = reee.index([[6]])
ff+=1
ss+=1
print(ff * ss)


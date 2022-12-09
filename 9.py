# im gna cry
import sys
sys.stdin = open("inp.txt", "r")

e = [[2000,2000] for i in range(10)]


vis = [[0] * 4000 for i in range(4000)]


def ok(i,j):
	hx = e[j][0]
	hy=	e[j][1]
	tx = e[i][0]
	ty = e[i][1]

	# conn

	if tx + 1 == hx and ty + 1 == hy:
		return True
	elif tx - 1 == hx and ty - 1 == hy:
		return True
		pass
	elif tx-1==hx and ty+1==hy:
		return True
	elif tx+1==hx and ty-1==hy:
		return True
		pass
	elif tx == hx and ty == hy:
		return True
		pass
	elif tx + 1 == hx and hy == ty:
		return True
		pass
	elif tx - 1 == hx and hy == ty:
		return True
		pass
	elif ty + 1 == hy and hx == tx:
		return True
		pass
	elif ty - 1 == hy and hx == tx:
		return True
		pass

	if hx == tx and hy + 1 == ty:
		return True
		pass
	elif hx == tx and hy - 1 == ty:
		return True
		pass
	elif hy == ty and hx + 1 == tx:
		return True
		pass
	elif hy == ty and hx - 1 == tx:
		return True
		pass
	
	return False

def move(j,i):
	hx = e[i][0]
	hy=	e[i][1]
	tx = e[j][0]
	ty = e[j][1]

	if hx != tx and hy != ty:
		if hx > tx: tx += 1
		elif hx < tx: tx -= 1

		if hy > ty: ty += 1
		elif hy < ty: ty -= 1
	elif hx == tx:
		if ty + 2 == hy:
			ty += 1
		elif ty - 2 == hy:
			ty -= 1
		else:
			print("NANI")
	elif hy == ty:
		if tx + 2 == hx:
			tx += 1
		elif tx - 2 == hx:
			tx -= 1
		else:
			print("NANI2")
	e[i][0]=hx
	e[i][1]=hy
	e[j][0]=tx
	e[j][1]=ty
		

vis[0][0]=1

for _ in range(2000):
	s = input().split()
	dirr = s[0]
	for i in range(int(s[1])):
		if (dirr == 'U'): e[9][1] += 1
		elif dirr == 'D': e[9][1] -= 1
		elif dirr == 'L': e[9][0] -= 1
		elif dirr == 'R': e[9][0] += 1

		for j in range(8, -1, -1):
			if not ok(j, j+1):
				move(j, j+1)
		
		# print(tx,ty)
		# print(tx,ty,hx,hy, ok())
		vis[e[0][0]][e[0][1]] = 1

	# for j in range(10):
		# print(e[j])j
	# print("so coko")
ans = 0
for i in vis:
	ans += sum(i)
print(ans-1)




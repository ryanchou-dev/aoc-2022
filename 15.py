import sys
sys.stdin = open("inp.txt", "r")

minx = float('inf')
miny = float('inf')
maxx=-float('inf')
maxy=-float('inf')

lg = -float('inf')

e = []
for i in range(38):
	s = input()

	x = int(s.split(',')[0].split('=')[-1])
	y = int(s.split(':')[0].split('=')[-1])
	x1 = int(s.split(',')[1].split('=')[-1])
	y1 = int(s.split(':')[1].split('=')[-1])
	lg = max(lg, abs(x-x1)+ abs(y-y1))

	minx = min(minx, x,x1)
	miny = min(miny, y,y1)
	maxx = max(maxx, x1,x)
	maxy = max(maxy, y1,y1)
	e.append([x,y,x1,y1])

# print(minx)
# print(miny)


dx = [1,0,-1,0]
dy = [0,1,0,-1]
zed = set()
# for i in e:
# 	dst = abs(i[0]-i[2]) + abs(i[1]-i[3])
# 	cr = dst
# 	toppy = i[1]
# 	while (cr >= 0):
# 		if toppy ==2000000:
# 			print(i[0]-cr, i[0]+cr+1)
# 			for j in range(i[0]-cr, i[0]+cr+1):
# 				if (j == i[2] and toppy == i[3]):
# 					continue
# 				zed.add((j, toppy))
# 		cr -= 1
# 		toppy -= 1
# 	cr = dst
# 	toppy = i[1]
# 	while (cr >= 0):
# 		if toppy ==2000000:
# 			print(i[0]-cr, i[0]+cr+1)
# 			for j in range(i[0]-cr, i[0]+cr+1):
# 				if (j == i[2] and toppy == i[3]):
# 					continue
# 				zed.add((j, toppy))
# 		cr -= 1
# 		toppy += 1
for i in e:
	dst = abs(i[0]-i[2]) + abs(i[1]-i[3])
	for j in range(dst + 1):
		for k in range(4):
			nx = i[0] + j * dx[k]
			ny = i[1] + ((dst+1)-j) * dx[k]
			if 0 <= nx <= 4000000 and 0 <= ny <= 4000000:
				gg = 0
				for qq in e:
					nwww = abs(qq[0]-nx) + abs(qq[1]-ny)
					if nwww <= abs(qq[0]-qq[2]) + abs(qq[1]-qq[3]):
						gg = 1
						break
				if not gg:
					print(nx * 4000000 + ny)
					exit()




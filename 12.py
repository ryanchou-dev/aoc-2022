import sys

sys.stdin = open('inp.txt', 'r')

# 41 * 132

gr = [['!' for i in range(132)] for j in range(41)]

st=[]
ed=[]
for i in range(41):
	s = input()
	for j in range(132):
		gr[i][j] = s[j]
		if (s[j] == 'S' or s[j] == 'a'):
			st.append([i, j])
			gr[i][j]='a'
		elif (s[j] == 'E'):
			ed = [i, j]
			gr[i][j]='z'

# find minimum path from st to ed given that you can only move to adjacent cells with adjacent letters
# BFS

	ans = float('inf')
for x in st:

	# i, j, dist
	vis = [[float('inf') for i in range(132)] for j in range(41)]

	todo = []
	todo.append([x[0], x[1], 0])

	while (len(todo) > 0):

		cur = todo.pop(0)
		if (cur[0] == ed[0] and cur[1] == ed[1]):
			ans = min(ans, cur[2])
			break
		if (cur[2] >= vis[cur[0]][cur[1]]):
			continue

		vis[cur[0]][cur[1]] = cur[2]
		# up

		if (cur[0] > 0 and vis[cur[0]-1][cur[1]] > cur[2]+1 and (ord(gr[cur[0]][cur[1]]) > ord(gr[cur[0]-1][cur[1]]) or abs(ord(gr[cur[0]][cur[1]]) - ord(gr[cur[0]-1][cur[1]])) <= 1)):
			todo.append([cur[0]-1, cur[1], cur[2]+1])
		# down
		if (cur[0] < 40 and vis[cur[0]+1][cur[1]] > cur[2]+1 and (ord(gr[cur[0]][cur[1]]) > ord(gr[cur[0]+1][cur[1]]) or abs(ord(gr[cur[0]][cur[1]]) - ord(gr[cur[0]+1][cur[1]])) <= 1)):
			todo.append([cur[0]+1, cur[1], cur[2]+1])
		# left
		if (cur[1] > 0 and vis[cur[0]][cur[1]-1] > cur[2]+1 and (ord(gr[cur[0]][cur[1]]) > ord(gr[cur[0]][cur[1]-1]) or abs(ord(gr[cur[0]][cur[1]]) - ord(gr[cur[0]][cur[1]-1])) <= 1)):
			todo.append([cur[0], cur[1]-1, cur[2]+1])
		# right
		if (cur[1] < 131 and vis[cur[0]][cur[1]+1] > cur[2]+1 and (ord(gr[cur[0]][cur[1]]) > ord(gr[cur[0]][cur[1]+1]) or abs(ord(gr[cur[0]][cur[1]]) - ord(gr[cur[0]][cur[1]+1])) <= 1)):
			todo.append([cur[0], cur[1]+1, cur[2]+1])



print(ans)

			

import sys

sys.stdin = open("inp.txt", "r")

ans = 0
for i in range(100):
	x = input()
	y = input()
	z = input()
	ok = 0

	qq = set()
	ww = set()
	ee = set()
	
	for j in x: qq.add(j)
	for j in y: ww.add(j)
	for j in z: ee.add(j)

	aaa = qq.intersection(ww, ee)			
	
	if (len(aaa) != 1): print("ANGHSDGH")

	aaa = list(aaa)
	zzz = aaa[0]
	if (ord(zzz) >= 97):
		ans += ord(zzz)-97+1
	else:
		ans += ord(zzz)-65+1+26
print(ans)
				

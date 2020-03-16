pw ={}
def r_r(sdat,fr,to,by):
	dat = sdat.split(' ')
	r=0
	for i in range(fr,to,by):
		pw[i] = dat[r]
		r+=1

r_r('1 a 3 9', 0, 4, 1)
r_r('d a c e 5 9 1 1' ,4, 20, 2)
r_r('6 c 2 9 0 2 b d 9', 5, 30, 3)
r_r('6 b d 0 a 9 9 6 b', 5, 40, 4)
r_r('a 5 1 2 2 3', 6, 40, 6)
r_r('a',7,8,1)
r_r('e d 1 a 6 9 c 8 b b', 10, 40, 3)
r_r('e b 2 9 2 d',10,40,5)
r_r('b a 8 6 e',15,40,6)
r_r('2 b d 9 7 d 0',20,40,3)

print pw
s=''
for key, value in pw.iteritems():
	print key,value
	s = s+value

print s

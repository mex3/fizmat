
#359 почти сделано
a = int(input())#number of athlets
c = []
while a > 0:
    a-=1
    b = map(str, input().split())
    c.append(b)
print(b)#print list of imposed data
m = []
for i in b:
    n = ' '.join(i)
    m.append(n)
for i in m:
    i = int()
u = max(m)
print(count(u))
#359
a, b = map(int,input().split(" "))
r = [ ]
for i in range(a):
    q = list(map(int,input().split(' ')))
    m = max(q)
    r.append(m)
w = max(r)
o = 0
for i in range(a):
    if r[i]== w:
        o += 1
print(o)
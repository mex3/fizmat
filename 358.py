
#№358 пытался
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
u = m.index(max(m))
m = u-2//3
print(m)
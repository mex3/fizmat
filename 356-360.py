#http://informatics.mccme.ru/mod/statements/view.php?id=15232#1
#решить несколько задач из 5

№356

n, m = input().split()
n = int(n)
m = int(m)
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    for k in range(m):
        a[i][k] = int(a[i][k])
summ = []
for i in range(n):
    summ.append(sum(a[i]))
print(max(summ))
print(summ.index(max(summ)))


№357

n, m = input().split()
n = int(n)
m = int(m)
a = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    for k in range(m):
        a[i][k] = int(a[i][k])
maxx=[]
for i in range(n):
    maxx.append(max(a[i]))
max0=max(maxx)
print(max0)
max1 = maxx.index(max0)
max2 = a[max1].index(max0)
print(max1, max2)


№358 пытался
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

#360
a, b = map(int,input().split(" "))
r = [ ]
for i in range(a):
    q = list(map(int,input().split(' ')))
    m = max(q)
    r.append(m)
w = max(r)
o = 0
e = [ ]
for i in range(a):
    if r[i]== w:
        o += 1
        e.append(i)
print(o)
for i in range(len(e)):
    print(e[i])

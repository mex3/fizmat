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
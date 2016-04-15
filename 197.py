l = input()               

x, y = list(map(int, input().split())
m = []
a = list(range(l, 0, 1))
for i in range(l, -1, -1):
    m.append(str(a[x[i]]))
    del a[x[i]]
m.reverse()
print(' '.join(m))




№197
k = int(input())                         
r = q = list(map(int, input().split())) 
m = [] 
n = list(range(k, 0, -1)) 
for i in range(k-1, -1, -1): 
    m.append(str(n[r[i]])) 
    del n[r[i]] 
m.reverse() 
print(' '.join(m)) 


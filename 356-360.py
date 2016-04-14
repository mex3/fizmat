#http://informatics.mccme.ru/mod/statements/view.php?id=15232#1
#решить несколько задач из 5

#356

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


#357

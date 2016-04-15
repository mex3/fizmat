#Проходит 72 из 100, остальные-ошибка.
import math
def dele(n,de):
  if n%de==0:
    return False
  elif de>=math.sqrt(n):
    return True
  else:
    return dele(n,de+1)

def IsPrime(n):
    de = 2
    return dele(n,de)

a = int(input().strip())
if IsPrime(a):
  print("YES")
else:
  print("NO")




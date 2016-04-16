#Проходит 72 из 100, остальные-ошибка.
import math
def dele(n,de):
  #Функция проверяет, делится ли число n на какое-то из чисел от 2 до корня из n
  if n%de==0:
    return False #Если число делится,оно составное
  elif de>=math.sqrt(n):
    #Если делитель превышает корень из самого числа, то оно простое
    return True
  else:
    return dele(n,de+1) 
    #Вызывается та же функция для следующего делителя(+1)

def IsPrime(n):
    de = 2
    return dele(n,de)

a = int(input().strip())
if IsPrime(a):
  print("YES")
else:
  print("NO")

#def IsPrime(n): 
    i = 2 
    while n % i != 0: 
        i = i + 1 
    if i == n: 
        return 'YES'#Тут нет рекурсии)) 
    else: 
        return 'NO' #обидно(((
  
print(IsPrime(int(input()))) 




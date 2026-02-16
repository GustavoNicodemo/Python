##2.1
from typing import Any
soma = 0
for i in range(5):
    soma = (i+1) + soma

print(soma)

##2.2

Sara= 23
Mark= 19
Fatima = 31

idades = [Sara, Mark, Fatima]

print(sum(idades) / len(idades))

##2.1c-g
print(403//73)
print(403%73)
print(2**10)
print(abs(54-57))
print(min([34.99, 29.95, 31.50]))

## 2.2

print(4 < 2+2)

C22ba = 7//3
C22bb = 1+1
print(C22ba == C22bb)

print(25 == 3**2 + 4**2)

print(12 < 2+4+6)

C22e = 1387 // 19
if C22e == 0:
    print("Div True")
else:
    print("Div False")

C22f = 31 // 2
if C22e == 0:
    print("Par")
else:
    print("Impar")

C22g = min([34.99, 29.95, 31.50])

if C22g <= 30:
    print("Maior Igual")
else:
    print("Menor")

##2.3

 a= int(3)
 b= 4

 c = a*a + b*b

 print(c)

 ##2.4

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
s4 = ' '

sa = s1 + s4 + s2 + s4 + s3
print(sa)

sb = (s1+s4)*11
print(sb)

sc = (s1+s4)*1 + (s2+s4)*2 + (s3+s4)*3
print(sc)

sd = (s1 + s4+ s2+ s4)*7
print(sd)

se = 5*(s2*2+s3+s4)
print(se)

##2.5
s = '0123456789'

print (s[0], s[1] , s[6], s[8], s[9])
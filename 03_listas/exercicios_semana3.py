##2.6

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

print(min(palavras))
print(max(palavras))

##2.7

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7))

notas[-1] = 5
print(notas)

print(max(notas))

notas.sort()
print(notas)

print(sum(notas) / len(notas))

##2.9

a29 = False + True
print(type(a29))

b29 = 2 * 3**2.0
print(type(b29))

c29 = 4 // 2 + 4 % 2
print(type(c29))

d29 = 2 + 3 == 4 or 5 >= 5
print(type(d29))

##2.10

a=6
b=8

import math

c = math.sqrt(a**2 + b**2)
print(c)

if c==5:
    print("Sim")
else:
    print("Não")

Area = (a**2)*math.pi
print(Area)

r=3

x = 3
y = 8

distancia = math.sqrt((x-a)**2+(y-b)**2)

if distancia == r:
    print("Na Circunferência")
elif distancia < r:
    print("Dentro da Circunferência")
else:
    print("Fora da Circunferência")

## Avaliativa

letra1 = 0, 1
letra2 = ('A','B')
letra3 = 'A'
letra4 = ('A')

print(type(letra1))
print(type(letra2))
print(type(letra3))
print(type(letra4))
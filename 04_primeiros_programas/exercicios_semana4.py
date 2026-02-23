## 3.1

try:
    temp_c = float(input("Digite a temperatura em graus Fahrenheit: "))
    temp_f = (temp_c * 9/5) + 32

    print(f"A temperatura em graus Celsius é {temp_f:.2f}")

except ValueError:

    print("Erro: Por favor, digite apenas números válidos.")

## 3.8

def media(numbers):
    return sum(numbers) / len(numbers)

numeros = [3, 3, 5]

print(f"{media(numeros):.3f}")

##3.9
import math

def perimetro(f_raio):
    f_perimetro = 2 * math.pi * f_raio
    return f_perimetro

raio = 1

print(f"O Perimetro é = {perimetro(raio):.4f}")

##3.10

def negativos(f_numeros):

    for i in range(len(f_numeros)):
        if f_numeros[i] < 0:
            print(f_numeros[i])

numeros = [-1, 2, -3, 4,-5]
negativos(numeros)

##3.11 e 3.12

def troca_posicao(lista):
    temp = lista[0]
    lista[0] = lista[-1]
    lista[-1] = temp
    print(lista)

time = ["Ava", "Eleanor", "Clare", "Sarah"]
troca_posicao(time)

ingredientes = ["farinha", "açúcar", "manteiga", "maçãs"]
troca_posicao(ingredientes)

##Entendendo alocação de Listas

lista1 = [1, 2, 3]
lista2 = lista1

lista1.append(10)

lista1 = [5, 8, 9]

print(lista1)
print(lista2)

##

def inverter(lista):
    lista.reverse()
    print(lista)

time = ["Ava", "Eleanor", "Clare", "Sarah"]
inverter(time)


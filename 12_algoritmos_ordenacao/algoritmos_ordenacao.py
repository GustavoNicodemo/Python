# Algoritmos de Ordenação
# Semana 12
import time


def teste(lista):
    erro = 0
    for k in range(1,len(lista)):
        if lista[k-1] > lista[k]:
            erro += 1
            print(f"rodo {erro} vezes")
    if erro == 0:
        print(f"Tudo Certo")
    else:
        print(f"Ordenação Errada {erro} vezes")


BaseTeste = [
    42, 7, 91, 13, 65, 28, 99, 3, 74, 56,
    18, 87, 31, 60, 5, 95, 22, 71, 40, 11,
    84, 52, 1, 67, 36, 98, 25, 79, 14, 58,
    93, 8, 47, 69, 20, 100, 33, 76, 2, 54,
    89, 16, 62, 45, 97, 27, 73, 10, 50, 81,
    6, 94, 38, 66, 24, 88, 15, 57, 92, 30,
    70, 4, 49, 83, 19, 61, 35, 96, 26, 78,
    12, 55, 90, 32, 68, 21, 85, 44, 9, 63,
    37, 72, 17, 53, 86, 29, 64, 41, 80, 23,
    59, 34, 75, 46, 82, 39, 77, 43, 51, 48
]

## BubbleSort
## Gustavo

Start = time.time()

# j = 1
# while j < len(BaseTeste):
#     for i in range (1,len(BaseTeste)):
#         if BaseTeste[i-1] > BaseTeste[i]:
#              temp = BaseTeste[i-1]
#              BaseTeste[i-1] = BaseTeste[i]
#              BaseTeste[i] = temp
#     j += 1


# for i in range(len(BaseTeste)-1):
#     for j in range(len(BaseTeste)-i-1):
#         if(BaseTeste[j] > BaseTeste[j+1]):
#             BaseTeste[j], BaseTeste[j+1] = BaseTeste[j+1], BaseTeste[j]

for m in range(1, len(BaseTeste)):
    chave = BaseTeste[m]
    n = m - 1
    while n >= 0 and chave < BaseTeste[n]:
        BaseTeste[n + 1] = BaseTeste[n]
        n -= 1
    BaseTeste[n + 1] = chave



Stop = time.time()

print(BaseTeste)
print(Stop-Start)
teste(BaseTeste)






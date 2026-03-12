# Exercícios Semana 7 - Vetores e Matrizes

## 4.1

s = "0123456789"

print("\nExercicio 4.1 \n")
print(f"A = {s[2:(4+1)]}")
print(f"B = {s[7:(8+1)]}")
print(f"C = {s[1:(7+1)]}")
print(f"D = {s[0:(3+1)]}")
print(f"E = {s[7:(9+1)]}")

## 4.2

previsao = 'It will be a sunny day today'

print("\nExercicio 4.2 \n")
print(f"A = {previsao.count("day")}")

clima = previsao.find("sunny")

print(f"B = {clima}")

troca = previsao.replace("sunny","cloudy")

print(f"C = {troca}")

## 5.9

def soma2D(V1,V2):
    soma = [[0 for _ in range(len(V1[0]))] for _ in range(len(V1))]
    for i in range(len(V1)):
        for j in range(len(V1[0])):
            soma[i][j] = V1[i][j] + V2[i][j]
    return soma

lista_t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
lista_s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]

lista_st = soma2D(lista_t,lista_s)

print("\nExercicio 5.9 \n")
for k in lista_st:
    print(k)
def acharDivisores(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    print(f"Divisores sao {divisores}")
    return divisores

# Soma de Fraçoes
# fração 2/3 + 3/4
a = 2
b = 5

c = 8
d = 15

denominador = b * d

numA = a * (denominador / b)

numB = c * (denominador / d)

numerador = (numA + numB)

print(f"{numerador=}")
print(f"--------------")
print(f"{denominador=}")

divNumerador = acharDivisores(int(numerador))
divDenominador = acharDivisores(int(denominador))

divComum = []

for i in divDenominador:
    for j in divNumerador:
        if i == j:
            divComum.append(i)

for k in divComum:
    numerador = numerador / k
    denominador = denominador / k

print("*"*30)
print(f"{numerador:>5.0f}")
print(f"--------")
print(f"{denominador:>5.0f}")
print("*"*30)


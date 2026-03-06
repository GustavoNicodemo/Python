#Converter numeros para /binario

numero = float(input("Digite um numero para ser convertido: "))
numeroDecimal = numero
binario = []

while True:
    if numero == 1 or numero == 0:
        binario.append(int(numero))
        binario.reverse()
        break
    print(f"O numero a se divido é: {numero}")

    if numero % 2 == 1:
        numero = numero // 2
        print(f"resto 1 e resultado {numero}")
        binario.append(1)
        continue
    elif numero % 2 == 0:
        numero = numero // 2
        print(f"Resto 0 e resultado {numero}")
        binario.append(0)
        continue

print("#"*30)
print(f"O numero {numeroDecimal} em binario é: ",end='')
print("".join(map(str, binario)))
print("#" * 30)


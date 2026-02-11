Notas = [3.6, 8.9, 10]

#Leitura = float(input("Digite a Nota 1: "))
#Notas.append(Leitura)

#Leitura = float(input("Digite a Nota 2: "))
#Notas.append(Leitura)

#Leitura = float(input("Digite a Nota 3: "))
#Notas.append(Leitura)

#Amort = float(input("Digite a Amortização: "))
Amort = 4

Numerador = 3

Denominador = (1 / (Notas[0] + Amort)) + (1 / (Notas[1] + Amort)) + (1 / (Notas[2] + Amort))

Media = (Numerador / Denominador) - Amort

print("A média final é: ", Media)

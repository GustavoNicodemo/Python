# Estruturas de Repetição (for, while)
# Semana 6
from operator import truediv

# Exemplo de while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Exemplo de for
for i in range(5):
    print(f"Iteração: {i}")


##

for i in ["Gato",2,5]:
    print(f"Index: {i}")
print("Fim.")


for j in range(1, 6, 2):
    print(f"Index: {j}")
print("Fim.")

##

Soma = 0

for k in range(0, 101):  # até 101 para incluir o 100
    if k%2 == 0:
        Soma = Soma + k

print(f"Soma: {Soma:.1f}")

##
nomesLista = ["Joesley" , "Purga" , "aguiar"]

print("Vogais :", end="")
for nome in nomesLista:
    for vogal in nome:
        if vogal in "aeiou":
        print(f", {vogal}", end="")

print("")
print("Fim.")

##

limite = 125
fatorial = 1
f = 1

while fatorial <= limite:
    f += 1
    fatorial = fatorial * f


print(f"f = {f-1}! = {int(fatorial/(f))}")

##

entrada = eval(input(f"Digite um número maior que 0: "))

while entrada <= 0:
    entrada = eval(input(f"Digite um número maior que 0: "))

print("Tudo Certo!")


##

nomesLista = []

#adicionaNome = input(f"Diga os nomes: }")
adicionaNome = "Inicial"

while adicionaNome != "":
    adicionaNome = input("Diga os nomes: ")
    if adicionaNome != "":
        nomesLista.append(adicionaNome)

print(f"Nomes: {nomesLista}")
print("Fim")

##
numero = 7

# def isPrimo(numero):
#     interacao = 2
#     while interacao < numero:
#         if numero % interacao == 0:
#             break
#     interacao += 1
#
#     return interacao == numero
#
# print(isPrimo(numero))
print("Fim")

##

b=0

for a in range(12):

    b += 1
    if b >= 9:
        print(f">>>{b=}")
        continue  ## força a nova interação independente da validaçao do segundo if
    else:
        print(f"<<<{b=}")

    if  b > 5:
        print("break")

##

def isPrimo(numero):
    interacao = 2
    while interacao < numero:
        if numero % interacao == 0:
            break
        interacao += 1
    return interacao == numero

faixa = 100
inicioTeste = 0

print(isPrimo(61))

for inicioTeste in range(999):
    isNumeroPrimo = isPrimo(inicioTeste)
    if isNumeroPrimo == False:
        continue

    print(f"É Número primo: {inicioTeste}")

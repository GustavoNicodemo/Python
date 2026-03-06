# Exercícios Semana 6 - Estruturas de Repetição
# Pratique os conceitos de for e while aqui

##

listaPalavra = []
listaImpressao = []

palavra = input("Digite uma palavra ou Null para encerrar: ")
listaPalavra.append(palavra)

while palavra != "":
    palavra = input("Digite uma palavra ou Null para encerrar: ")
    listaPalavra.append(palavra)

for i in range(len(listaPalavra)):
    if len(listaPalavra[i]) == 4:
        listaImpressao.append(listaPalavra[i])

print(f"As palavras de 4 letras são: {listaImpressao}")

##
a = 10
b = 2

for j in range(a):
    print(f" a-> {j}")

print("")

for j in range(b):
    print(f" b-> {j}")

##

a1=3 ; a2=12
for i in range(a1,a2+1):
    print(f"a - {i}")
print("")

b1=0 ; b2=9 ; bStep=2
for i in range(b1,b2,bStep):
    print(f"b - {i}")
print("")

c1=0 ; c2=24 ; cStep=3
for i in range(c1,c2,cStep):
    print(f"c - {i}")
print("")

d1=3 ; d2=12 ; dStep=5
for i in range(d1,d2,dStep):
    print(f"d - {i}")

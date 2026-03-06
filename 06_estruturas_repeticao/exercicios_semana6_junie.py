# Exercícios Semana 6 - Estruturas de Repetição (Versão Melhorada por Junie)
# Este arquivo contém as mesmas funcionalidades do arquivo original, mas com melhorias em legibilidade e eficiência.

## --- Exercício 1: Filtrar palavras de 4 letras ---
print("--- Exercício 1 ---")
lista_palavras = []

while True:
    # O prompt sugere 'Null' ou apenas Enter para encerrar. 
    # Vou considerar string vazia como critério de saída, conforme o código original.
    entrada = input("Digite uma palavra (ou pressione Enter para encerrar): ").strip()
    
    if entrada == "" or entrada.lower() == "null":
        break
    
    lista_palavras.append(entrada)

# Melhoria: Usando List Comprehension em vez de loop for + append manual
# É mais rápido e legível em Python.
palavras_4_letras = [p for p in lista_palavras if len(p) == 4]

print(f"As palavras de 4 letras encontradas são: {palavras_4_letras}")
print("\n" + "="*30 + "\n")


## --- Exercício 2: Loops Simples ---
print("--- Exercício 2 ---")
a = 10
b = 2

# Iteração direta e uso de f-strings mantidos, mas com nomes de variáveis mais claros
for i in range(a):
    print(f"a -> {i}")

print("")    

for i in range(b):
    print(f"b -> {i}")

print("\n" + "="*30 + "\n")


## --- Exercício 3: Loops com Range Customizado (Início, Fim, Passo) ---
print("--- Exercício 3 ---")

# Caso A: de 3 a 12 inclusive
print("Sequência A (3 a 12):")
for i in range(3, 13): # range(start, stop) - stop não é incluído, por isso usamos 13
    print(f"a - {i}")
print("") 

# Caso B: de 0 a 9 com passo 2 (exclui o 9)
print("Sequência B (0 a 8, passo 2):")
for i in range(0, 9, 2):
    print(f"b - {i}")
print("") 

# Caso C: de 0 a 24 com passo 3 (exclui o 24)
print("Sequência C (0 a 21, passo 3):")
for i in range(0, 24, 3):
    print(f"c - {i}")
print("") 

# Caso D: de 3 a 12 com passo 5
print("Sequência D (3, 8):")
for i in range(3, 12, 5):
    print(f"d - {i}")

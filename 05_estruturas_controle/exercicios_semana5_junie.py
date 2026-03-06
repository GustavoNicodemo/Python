# Exercícios Semana 5 - Estruturas de Controle (Versão Melhorada por Junie)
# Este arquivo contém as mesmas funcionalidades do arquivo original, mas com melhorias em segurança e robustez.

## --- Exercício 3.4: Login ---
print("--- Exercício 3.4: Login ---")

# Melhoria: .strip() para remover espaços e .lower() para comparação case-insensitive (opcional, mas comum)
login = input("Digite o Usuário: ").strip()

# Melhoria: Removi o espaço acidental em ' hani'
# Se o usuário digitasse 'hani', o original não encontraria por causa do espaço extra na lista.
userList = ['joe', 'sue', 'hani', 'sophie']

if login in userList:
    print(f"Login: {login}")
    print("Você entrou!")
else:
    print(f"Login: {login}")
    print("Usuário desconhecido.")

print("Fim.")
print("\n" + "="*30 + "\n")


## --- Exercício 5.1: IMC ---
print("--- Exercício 5.1: IMC ---")

def calcular_imc(peso, altura):
    """Calcula o IMC e retorna o valor."""
    return peso / (altura ** 2)

# Melhoria: Substituindo eval() por float() para maior segurança.
# O eval() pode executar código arbitrário e é perigoso em programas reais.
# Também adicionei um bloco try/except para evitar erros se o usuário digitar letras no lugar de números.

try:
    altura_str = input("Altura em metros (ex: 1.75): ").replace(',', '.') # Lida com quem usa vírgula
    altura = float(altura_str)
    
    peso_str = input("Peso em kg (ex: 70.5): ").replace(',', '.')
    peso = float(peso_str)

    if altura <= 0 or peso <= 0:
        print("Erro: Peso e altura devem ser valores positivos.")
    else:
        resultado = calcular_imc(peso, altura)

        # Classificação do IMC
        if resultado < 18.5:
            classificacao = "Abaixo do Peso"
        elif resultado < 25:
            classificacao = "Normal"
        elif resultado < 30: # Adicionei uma categoria intermediária para ficar mais completo
            classificacao = "Sobrepeso"
        else:
            classificacao = "Acima do Peso (Obesidade)"

        print(f"Classificação: {classificacao}")
        print(f"O Valor do IMC é {resultado:.2f}")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos para peso e altura.")

print("\nFim do programa.")

## 3.4 Login

login = input("Digite o Usuário:")

userList = ['joe', 'sue', ' hani', 'sophie']

if login in userList:
    print(f"Login: {login}")
    print("Você entrou!")
else:
    print(f"Login: {login}")
    print("Usuário desconhecido.")

print("Fim.")

## 5.1 IMC

def  meuIMC(peso,altura):
    imc = peso / (altura ** 2)
    return imc

altura = eval(input("Altura em metros: "))
peso = eval(input("Peso em kg: "))

resultado = meuIMC(peso, altura)

if resultado < 18.5:
    print("Abaixo do Peso")
elif resultado < 25:
    print("Normal")
else:
    print("Acima do Peso")

print(f"O Valor do IMC é {resultado:.2f}")

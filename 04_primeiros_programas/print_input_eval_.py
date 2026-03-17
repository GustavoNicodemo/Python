h = 13
print("Agora são", h, 'horas', sep=".")

print("Agora são", h, 'horas')
print("Agora são", h, 'horas', end=">")
print("Agora são", h, 'horas', end=".\n\n")

print("Agora são", h, 'horas')

##

x = input ("Digite um numero: ")

print(type(x))

x = eval(x)

print(type(x))

print(x)

## Calculo Temperatura de Celsius para Farenheint

temp_c = eval(input("Digite a temp. em Celsius: "))
temp_f = (temp_c * 9/5) + 32
temp_k = temp_c + 273.15

print("Temperatura em Farenheint: ", temp_f,"\nTemperatura em Kelvin: ", temp_k)
##

def media(x, y, z):
    return (x + y + z) / 3


try:
    # Caso queira testar com entrada do usuário, use:
    # x = float(input("Digite o primeiro número: "))
    # y = float(input("Digite o segundo número: "))
    # z = float(input("Digite o terceiro número: "))

    x = 1
    y = 1
    z = 2

    resultado = media(x, y, z)
    # Correção: A aspa final deve vir APÓS o fechamento da chave }
    print(f"A média dos números é: {resultado:.3f}")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")

## Testes de f-string


numeroPi = 3.14159
print(f"pi = {numeroPi}")
print(f"{numeroPi = }")

print("-----------------")

n = 12345.6789

print(f"n = {n:.2f}")
print(f"n = {n:.0f}")
print(f"n = {n:,.2f}")
print(f"n = {n:_.2f}")
print(f"n = {n:.2e}")
print(f"n = {n:.2f}")
print(f"n = {n:+.2f}")
print(f"n = {n:+}")

print("-----------------")

p = 5.45

print(f"Porcentagem = {p:.2%}")
print(f"Porcentagem = {p:.0%}")

print("-----------------")

decimais = 3

print(f"Pi = {numeroPi:.{decimais}}")

print("-----------------")

texto = "Teste"

print(f"Texto = {texto:$<15}")
print(f"Texto = {texto:+>15}")
print(f"Texto = {texto:*^15}")

print("-----------------")

dec = 145

print(f"Binario = {dec = :b}")
print(f"Hexa = {dec = :x}")
print(f"Octa = {dec = :o}")
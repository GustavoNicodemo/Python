# Arquivo para a Semana 3
cpf = input("Digite seu CPF: ")

if len(cpf) == 11:
    verificador_1 = 0
    verificador_2 = 0

    for i in range(9):
         verificador_1 = verificador_1 + int(cpf[i])*(i+1)

    digito_10 = verificador_1 % 11
    if digito_10 == 10:
         digito_10 = 0

    for j in range(10):
         verificador_2 = verificador_2 + int(cpf[j])*(j)

    digito_11 = verificador_2 % 11
    if digito_11 == 10:
         digito_11 = 0

    if digito_10 == int(cpf[9]) and digito_11 == int(cpf[10]):
         print("O CPF passou no teste de verificação.")
    else:
          print("O CPF é invalido.")
else:
    print("O CPF é Invalido.")

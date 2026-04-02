def equacao(x):
    # Equação Avaliada # ------------------------

    y = x + 1

    # -------------------------------------------
    return y

def funcao(a, b, n):
    passo = (b-a) / n
    x = a
    valores_funcao = [0]*(n+1)
    for i in range(len(valores_funcao)):
        valores_funcao[i] = equacao(x)
        x += passo
    print(f"Função Calculada (X)")
    return valores_funcao

def integral_inf(a, b, n, resultado):
    passo = (b - a) / n
    soma = 0
    for i in range(len(resultado)-1):
        soma += resultado[i]*passo
    print(f"Integral Inferior Calculada (X)")
    return soma

def integral_sup(a, b, n, valores_funcao):
    passo = (b - a) / n
    soma = 0
    for i in range(1, len(valores_funcao)):
            soma += valores_funcao[i] * passo
    print(f"Integral Superior Calculada (X)")
    return soma


if __name__ == "__main__":
    print("\n--- Início ---")
    A = 1
    B = 3
    N = 1000000 # Nao exagerar no número hehehehe
    Valores_Funcao = funcao(A, B, N)

    Soma_Inf = integral_inf(A, B, N, Valores_Funcao)
    Soma_Sup = integral_sup(A, B, N, Valores_Funcao)

    print(f"Integral Def Inferior = {Soma_Inf}")
    print(f"Integral Def Superior = {Soma_Sup}")

    Media = (Soma_Inf + Soma_Sup) / 2

    print(f"Media Valor = {Media}")


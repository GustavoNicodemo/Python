##
def criartransposta(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    # Inicializa a matriz transposta com zeros (ou None)
    # A transposta terá n_colunas linhas e n_linhas colunas
    transposta = [[0 for _ in range(n_linhas)] for _ in range(n_colunas)] #Ajuda da Junie, precisa aprender direito.
    
    for i in range(n_linhas):
        for j in range(n_colunas):
            transposta[j][i] = matriz[i][j]
            
    return transposta

def issimetrica(matriz1):
    n_linhas = len(matriz1)
    n_colunas = len(matriz1[0])
    simetrica = True
    for i in range(n_linhas):
        for j in range(n_colunas):
            if matriz1[j][i] != matriz1[i][j]:
                simetrica = False
                break
    if simetrica == True:
        print("A Matriz é SIMÉTRICA")
    else:
        print("A Matriz não é SIMÉTRICA")
    return

matriz_teste = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

print("Matriz Original:")
for linha in matriz_teste:
    print(linha)

transposta_matriz_teste = criartransposta(matriz_teste)
print("\nMatriz Transposta:")
for linha in transposta_matriz_teste:
    print(linha)

issimetrica(matriz_teste)

##

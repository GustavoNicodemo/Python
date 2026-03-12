# Exercícios Semana 7 - Vetores e Matrizes (Sugestões da Junie)

"""
Olá! Refiz este arquivo focando exclusivamente nos exercícios da semana 7.
Incluí melhorias de legibilidade e boas práticas, mantendo o foco didático que você pediu.

Melhorias aplicadas:
1. Fatiamento Didático: No exercício 4.1, usei o formato (x+1) para destacar que o limite superior é exclusivo.
2. F-Strings: Para exibir os resultados de forma clara.
3. List Comprehension (5.9): Para somar as matrizes de forma eficiente e compacta.
4. Validação de Dimensões (5.9): Garante que as matrizes podem ser somadas antes de tentar a operação.
"""

# --- Exercício 4.1 ---
# Fatiamento de strings (Slicing)
def exercicio_4_1():
    print("\n--- Exercício 4.1 ---")
    s = "0123456789"
    
    # Nota didática: O uso de (x+1) deixa claro que o último índice informado não é incluído no fatiamento.
    print(f"A = {s[2:(4+1)]}")  # '234'
    print(f"B = {s[7:(8+1)]}")  # '78'
    print(f"C = {s[1:(7+1)]}")  # '1234567'
    print(f"D = {s[0:(3+1)]}")  # '0123'
    print(f"E = {s[7:(9+1)]}")  # '789'

# --- Exercício 4.2 ---
# Métodos de strings
def exercicio_4_2():
    print("\n--- Exercício 4.2 ---")
    previsao = 'It will be a sunny day today'
    
    # A) Contagem
    print(f"A (Ocorrências de 'day'): {previsao.count('day')}")
    
    # B) Busca (Índice)
    clima_idx = previsao.find("sunny")
    print(f"B (Índice de 'sunny'): {clima_idx}")
    
    # C) Substituição
    # Lembre-se: strings são imutáveis; replace() retorna uma cópia com a alteração.
    troca = previsao.replace("sunny", "cloudy")
    print(f"C (Substituição): {troca}")

# --- Exercício 5.9 ---
# Soma de matrizes 2D
def soma_matrizes_2d(m1, m2):
    """
    Soma duas matrizes se tiverem as mesmas dimensões.
    """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
    
    # Usando List Comprehension para realizar a soma de forma concisa.
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def exercicio_5_9():
    print("\n--- Exercício 5.9 ---")
    lista_t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
    lista_s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
    
    try:
        resultado = soma_matrizes_2d(lista_t, lista_s)
        print("Resultado da soma das matrizes:")
        for linha in resultado:
            print(linha)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    exercicio_4_1()
    exercicio_4_2()
    exercicio_5_9()

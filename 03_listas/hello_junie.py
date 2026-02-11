def saudacao(nome):
    """Retorna uma mensagem de saudação simples."""
    return f"Olá, {nome}! Bem-vindo ao exemplo da IA Junie."

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

if __name__ == "__main__":
    # Exemplo de uso das funções
    nome_usuario = "Gustavo"
    print(saudacao(nome_usuario))
    
    num1 = 10
    num2 = 5
    resultado = soma(num1, num2)
    print(f"A soma de {num1} e {num2} é: {resultado}")

    # Uma lista simples para demonstrar iteração
    frutas = ["Maçã", "Banana", "Cereja"]
    print("Minhas frutas favoritas:")
    for fruta in frutas:
        print(f"- {fruta}")


input("Pressione Enter para sair...")
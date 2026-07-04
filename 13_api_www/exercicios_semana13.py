# Exercícios Semana 13 - API e WWW
# Aluno: Gustavo

import urllib.request
import json

def exercicio_1():
    """
    Crie uma função que solicite ao usuário um CEP e exiba o logradouro e a cidade.
    """
    print("--- Exercício 1: Consulta de CEP ---")
    cep = input("Digite o CEP (apenas números): ")
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        with urllib.request.urlopen(url) as response:
            dados = json.loads(response.read().decode())
            if "erro" not in dados:
                print(f"Rua: {dados.get('logradouro')}")
                print(f"Cidade: {dados.get('localidade')} - {dados.get('uf')}")
            else:
                print("CEP inválido.")
    except:
        print("Erro ao conectar com a API.")

def exercicio_2():
    """
    Simule uma requisição GET para uma API de testes (JSONPlaceholder) 
    e liste o título dos 5 primeiros posts.
    """
    print("\n--- Exercício 2: Listar Posts (JSONPlaceholder) ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        with urllib.request.urlopen(url) as response:
            posts = json.loads(response.read().decode())
            for post in posts[:5]:
                print(f"Post {post['id']}: {post['title']}")
    except:
        print("Erro ao buscar posts.")

if __name__ == "__main__":
    # exercicio_1() # Comentado para não interromper fluxo automático se houver
    exercicio_2()

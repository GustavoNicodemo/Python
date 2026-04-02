# Estudos sobre Manipulação de Arquivos em Python

# Diferentes modos de abertura:
# 'r'  - Leitura (Padrão). Erro se o arquivo não existe.
# 'w'  - Escrita. Cria o arquivo ou sobrescreve se já existir.
# 'a'  - Append (Anexar). Adiciona ao final do arquivo sem apagar o anterior.
# 'x'  - Criação exclusiva. Erro se o arquivo já existir.
# 't'  - Modo texto (Padrão).
# 'b'  - Modo binário (Ex: imagens).
# '+'  - Abre para atualização (leitura e escrita).

def exemplo_leitura():
    print("Exemplo de leitura:")
    try:
        # Usar 'with' é a forma recomendada (context manager)
        with open('estudo.txt', 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo ainda não criado.")

def exemplo_escrita():
    print("Exemplo de escrita:")
    with open('estudo.txt', 'w', encoding='utf-8') as f:
        f.write("Este é um arquivo de estudo.\n")
        f.write("Aprendendo Python com a Junie!\n")

if __name__ == "__main__":
    exemplo_escrita()
    exemplo_leitura()

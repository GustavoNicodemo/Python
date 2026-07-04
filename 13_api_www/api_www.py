# Estudos sobre API e Protocolo HTTP
# Semana 13

import urllib.request
from html.parser import HTMLParser
import json
from encodings import utf_8


def buscar_dados_cep(cep):
    """
    Exemplo básico de consumo de API usando a biblioteca padrão urllib.
    Consome a API ViaCEP para buscar informações de um CEP.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        print(f"Buscando dados para o CEP: {cep}...")
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                dados = json.loads(response.read().decode())
                if "erro" not in dados:
                    return dados
                else:
                    return "CEP não encontrado."
            else:
                return f"Erro na requisição: Status {response.status}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def mostrar_exemplo():
    cep_teste = "01001000"  # Praça da Sé, SP
    resultado = buscar_dados_cep(cep_teste)

    if isinstance(resultado, dict):
        print("\nDados encontrados:")
        for chave, valor in resultado.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print(resultado)

def getSource(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html.decode()

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    print(attr[1])


if __name__ == "__main__":
    html = getSource("https://www.uol.com.br")
    #print(html)
    Parser = MyParser()
    Parser.feed(html)
    print(Parser)
    #mostrar_exemplo()

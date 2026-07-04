### Exercício 8.1

class Ponto:
    x = -1
    y = -1

    def getx(self):
        # print(f"Px = {p.x}")
        return self.x


p = Ponto()

p.getx()


### Exercício 8.2

class Teste:
    versao = 1.02


a = Teste()
b = Teste()


### Exercício 8.3

class Retangulo:
    comprimento = 0
    largura = 0

    def setTamanho(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def perimetro(self):
        return 2 * (self.largura + self.comprimento)

    def area(self):
        return self.largura * self.comprimento


ret = Retangulo()
ret.setTamanho(5, 2)

print(f"Perímetro = {ret.perimetro()}")
print(f"Área = {ret.area()}")


### 8.4

class Animal:

    def __init__(self, especie="animal", som="emitir sons"):
        self.especie = especie
        self.som = som

    def fala(self):
        print(f"Eu sou um {self.especie} e sei {self.som}")


snoopy = Animal('cão', 'latir')
snoopy.fala()

tweety = Animal('canário')
tweety.fala()

animal = Animal()
animal.fala()

### Exercício 8.5

from random import shuffle


class Carta:

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe


class Baralho:
    # representa um baralho de 52 cartas
    # valores e naipes são variáveis da classe Baralho

    valores = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = ('\u2660', '\u2661', '\u2662', '\u2663')

    def __init__(self):
        self.baralho = []  # baralho está inicialmente vazio

        for naipe in Baralho.naipes:  # naipes e valores são Baralho
            for valor in Baralho.valores:  # variáveis da classe
                # inclui Carta com certo valor e naipe no baralho
                self.baralho.append(Carta(valor, naipe))

    def distribuiCarta(self):
        return self.baralho.pop()

    def shuffle(self):
        shuffle(self.baralho)

poker = Baralho()

poker.shuffle()
# Estudos de Programação Orientada a Objetos (POO)

# 1. Definição de uma Classe
class Pessoa:
    # O método __init__ é o construtor da classe
    def __init__(self, nome, idade):
        self.nome = nome    # Atributo
        self.idade = idade  # Atributo

    # Método de instância
    def saudar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# 2. Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, idade)
        self.curso = curso

    # Sobrescrita de método (Polimorfismo)
    def saudar(self):
        print(f"Olá, sou o estudante {self.nome}, estudo {self.curso} e tenho {self.idade} anos.")

# 3. Encapsulamento (Convenção de prefixo _)
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo # Atributo "protegido"

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado.")

    def ver_saldo(self):
        return self._saldo

if __name__ == "__main__":
    # Instanciando objetos
    p1 = Pessoa("João", 30)
    p1.saudar()

    e1 = Estudante("Maria", 20, "Engenharia")
    e1.saudar()

    conta = ContaBancaria("Carlos", 1000)
    conta.depositar(500)
    print(f"Saldo atual: R${conta.ver_saldo()}")

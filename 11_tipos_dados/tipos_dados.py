# Estudo de Tipos de Dados (Pilha, Lista, Árvores) - Semana 11

# --- Pilha (Stack) ---
class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, item):
        self.itens.append(item)
    
    def desempilhar(self):
        return self.itens.pop()

# --- Lista Ligada (Linked List) ---
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# --- Árvore Binária (Binary Tree) ---
class NodoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

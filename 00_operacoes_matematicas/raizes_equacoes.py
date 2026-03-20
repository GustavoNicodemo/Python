
from math import sqrt

#Funções -------------------------------------------------------------------------------------

def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("\nNão existe Raízes Reais (Existem porém Complexas)")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"\nRaízes Reais e Iguais a {x1}")
        print(f"Eq. pode ser substituída por: {a}*(X{-x1:+})²")
    elif delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"\nDuas Raízes Reais a {x1} e {x2}")
        print(f"Eq. pode ser substituída por: {a}*(X{-x1:+})*(X{-x2:+})")

    print("\nFim Bhaskara.")
    return

def acha_minimo(novo_b, novo_c , passo , xi):
    while True:

        lista_x1 = [xi - passo, xi, xi + passo]

        for i in range(len(lista_x1)):
            lista_y1[i] = lista_x1[i] ** 2 + novo_b * lista_x1[i] + novo_c

        if lista_y1[0] > lista_y1[1] > lista_y1[2]:
            xi = xi + passo

        elif lista_y1[0] < lista_y1[1] < lista_y1[2]:
            xi = xi - passo

        elif lista_y1[0] > lista_y1[1] < lista_y1[2]:
            index_minimo = lista_y1.index(min(lista_y1))
            y_minimo = lista_x1[index_minimo]

            break

        # elif lista_y1[0] == lista_y1[1]:
        #     raiz = (lista_x1[0]+lista_x1[1])/2
        #     print("4")
        #     break
        #
        # elif lista_y1[1] == lista_y1[2]:
        #     raiz = (lista_x1[1]+lista_x1[2])/2
        #     print("5")
        #     break
    return y_minimo, lista_x1, lista_y1

def acha_raiz(novo_b, novo_c, passo, xi , yi):
     while True:
         yi[0] = xi ** 2 + novo_b * xi + novo_c
         if abs(yi[0]) > abs(yi[1]):
             break
         else:
             xi = xi + passo
             yi[1] = yi[0]
     return xi - passo

# Inicio do programa -------------------------------------------------------------------------

print("Seja a Eq. Ax² + Bx + C = 0")

Passo = 0.001
Xi = 0

try:
    Constante_A_str = input("Constante A: ").replace(',', '.')
    A = float(Constante_A_str)

    Constante_B_str = input("Constante B: ").replace(',', '.')
    B = float(Constante_B_str)

    Constante_C_str = input("Constante C: ").replace(',', '.')
    C = float(Constante_C_str)

    # A = 1
    # B = 0
    # C = -4
    # Algoritmo Bhaskara
    bhaskara(A , B , C)

    # Algoritmo de Iteração
    # Forçar A ser igual a 1 dividindo tudo por A
    Novo_B = B / A
    Novo_C = C / A

    lista_y1 = [999 , 999 , 999]

    Y_Minimo = acha_minimo( Novo_B, Novo_C, Passo, Xi)

    if Y_Minimo[2][1] < 0:
        Raiz = acha_raiz(Novo_B, Novo_C, Passo, Y_Minimo[1][1] , [0 , Y_Minimo[2][1]])
        Outra_Raiz = Y_Minimo[1][1] * 2 - Raiz
        print(f"\nIterativo: As raízes são: {Raiz:.4f} e {Outra_Raiz:.4f}")
    elif Y_Minimo[2][1] == 0:
        Raiz = acha_raiz(Novo_B, Novo_C, Passo, Y_Minimo[1][1], [0, Y_Minimo[2][1]])
        print(f"\nIterativo: Uma raiz dupla e igual a {Raiz:.4f)}")
    else:
        print(f"\nIterativo: Não tem Raízes Reais")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos para as constantes.")


# Exercícios de Interfaces Gráficas com Tkinter - Semana 14

"""
Exercício 1: Crie uma janela que contenha um contador. 
Ao clicar em um botão "+1", o valor exibido em um label deve aumentar.
"""

import tkinter as tk

Total = 2

def adicionar_contador():
    global Total
    Total = Total + 1
    label.config(text=f"{Total}")


# def subtrair_contador():
#     Total -= 1


# Criar a janela principal
root = tk.Tk()
root.title("Contador")
root.geometry("300x250")

# Criar widgets
botao = tk.Button(root, text="+1", command=adicionar_contador())
botao.pack(pady=10)

# botao = tk.Button(root, text="-1", command=subtrair_contador())
# botao.pack(pady=10)

label = tk.Label(root, text=f"{Total}")
label.pack(pady=12)

# Iniciar o loop principal
root.mainloop()

"""
Exercício 2: Crie um conversor de temperatura (Celsius para Fahrenheit).
O usuário digita o valor em Celsius, clica em um botão, e o resultado aparece em outro label.
"""

"""
Exercício 3: Crie uma pequena calculadora com botões para Somar, Subtrair, Multiplicar e Dividir
dois números inseridos pelo usuário.
"""

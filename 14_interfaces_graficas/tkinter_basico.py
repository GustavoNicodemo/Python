import tkinter as tk

def saudacao():
    label.config(text=f"Olá, {entry.get()}!")

# Criar a janela principal
root = tk.Tk()
root.title("Janelinha")
root.geometry("300x250")

# Criar widgets
label_instrucao = tk.Label(root, text="Digite seu nome:")
label_instrucao.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

botao = tk.Button(root, text="Clique", command=saudacao)
botao.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

# Iniciar o loop principal
root.mainloop()

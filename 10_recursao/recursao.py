# Estudo de Recursão - Semana 10

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    print(f"Fatorial de 5: {fatorial(5)}")

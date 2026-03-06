a = 650

while True:

    strChute = (input("chute um valor pra raíz: "))
    if strChute == "":
        break
    else:
        chute = int(strChute)

    erro = a - chute**2

    if erro == 0:
        print(f"acertou {chute**2}")
        break
    elif erro > 0:
        print(f"chute um valor maior {chute**2}")
    elif erro < 0:
        print(f"chute um valor menor {chute**2}")

print("Fim")
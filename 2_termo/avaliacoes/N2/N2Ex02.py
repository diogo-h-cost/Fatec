with open("contacorrente.txt", "r") as fil:
    saldo = 0
    for linha in fil:
        letra, sald = linha.split(" ")
        sald = float(sald)
        if letra == "C":
            saldo += sald
        elif letra == "D":
            saldo -= sald
        print(letra, sald)
    print(f"\nSaldo Final: R$ {saldo:.2f}")
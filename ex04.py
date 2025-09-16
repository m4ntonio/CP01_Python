nota = float(input("Digite sua nota (0 a 10): "))
if 0 <= nota <= 10:
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Nota inválida. Digite um valor entre 0 e 10.")
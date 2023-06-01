
saltos = []
while True:
    nome = input("Nome do atleta: \n")
    if nome == "":
        break
    s1 = float(input("Primeiro salto: "))
    s2 = float(input("Segundo salto: "))
    s3 = float(input("Terceiro salto: "))
    s4 = float(input("Quarto salto: "))
    s5 = float(input("Quinto salto: "))

    saltos.extend([s1, s2, s3, s4, s5])


    soma = sum(saltos)
    media = soma / 5

    print("\t Resultado final")
    print("Atleta: ", nome)
    print(f'Saltos: {s1:.1f} - {s2:.1f} - {s3:.1f} - {s4:.1f} - {s5:.1f}')
    print(f'Média dos saltos: {media:.1f}\n\n')


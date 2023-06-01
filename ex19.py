Windows_Server = []
Unix = []
Linux = []
Netware = []
Mac_OS = []
Outro = []

print("Para finalizar a votação, digite '0'")

while True:
    print('Possíveis candidatos\n')
    print('1- Windows Server')
    print('2- Unix')
    print('3- Linux')
    print('4- Netware')
    print('5- Mac OS')
    print('6- Outro')
    voto = int(input("Informe seu voto: "))
    if voto == 1:
        Windows_Server.append(1)
    elif voto == 2:
        Unix.append(1)
    elif voto == 3:
        Linux.append(1)
    elif voto == 4:
        Netware.append(1)
    elif voto == 5:
        Mac_OS.append(1)
    elif voto == 6:
        Outro.append(1)
    else:
        print('Voto invalido')
        
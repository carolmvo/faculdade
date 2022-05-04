from random import *
sorteio = randint(0, 2)
print("Bem vidos ao pedra papel tesoura 2.0!")
modo = int(input("Qual modo de jogo você gostaria de jogar OPC 1: (pvp) ou OPC 2: (computador)?  "))

if modo == 1:
    nome1 = input("Digite seu nome: ")
    nome2 = input("Digite seu nome: ")
    print(" PEDRA = 0\n PAPEL = 1\n TESOURA = 2")
    jogada1 = int(input(f"{nome1}, qual a sua jogada? "))
    print("\n\n\n\n\n\n\n\n")
    jogada2 = int(input(f"{nome2}, qual a sua jogada? "))

    if jogada1 > 2 or jogada1 < 0 and jogada2 > 2 or jogada2 < 0:
        print("JOGADA INVÁLIDA!")
    else:
        if jogada1 == jogada2:
            print("Empate!")
        else:
            if jogada1 == 0 and jogada2 == 1:
                print(f"{nome2} ganhou!")
            else:
                if jogada1 == 0 and jogada2 == 2:
                    print(f"{nome1} ganhou!")
                else:
                    if jogada1 == 1 and jogada2 == 2:
                        print(f"{nome2} ganhou!")
                    else:
                        if jogada1 == 1 and jogada2 == 0:
                            print(f"{nome1} ganhou!")
                        else:
                            if jogada1 == 2 and jogada2 == 0:
                                print(f"{nome2} ganhou!")
                            else:
                                if jogada1 == 2 and jogada2 == 1:
                                    print(f"{nome1} ganhou!")
else:
    nome = input("Digite seu nome: ")
    print(" PEDRA = 0\n PAPEL = 1\n TESOURA = 2")
    jogada = int(input("Digite sua jogada: "))

    if jogada < 0 or jogada > 2:
        print("JOGADA INVÁLIDA!")
    else:
        if jogada == sorteio:
            print("Empate!")
        else:
            if jogada == 0 and sorteio == 1:
                print("Computador ganhou!")
            else:
                if jogada == 0 and sorteio == 2:
                    print(f"{nome} ganhou!")
                else:
                    if jogada == 1 and sorteio == 2:
                        print("Computador ganhou!")
                    else:
                        if jogada == 1 and sorteio == 0:
                            print(f"{nome} ganhou!")
                        else:
                            if jogada == 2 and sorteio == 0:
                                print("Computador ganhou!")
                            else:
                                if jogada == 2 and sorteio == 1:
                                    print(f"{nome} ganhou!")
    print(f"O computador jogou {sorteio}!")


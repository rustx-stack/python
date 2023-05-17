#ANDRÉ DE SOUZA CALLEJÃO RM 99732

def menu():
    print(f'''
    MENU
    1 - Intervalo
    2 - Intervalo Aberto e Fechado
    3 - Intervalo em ordem crescente e decrescente
    0 - SAIR''')



def intervalo ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 < n2:
            print("[", end=" ")
            for i in range(n1, n2 + 1):
                print(f"{i} ", end="")
            print("[")

        elif n1 > n2:
            print("[", end=" ")
            for i in range(n2, n1 + 1):
                print(f"{i} ", end="")
                print("[")
        else:
            print(n1)


def intervalo_a_f():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    a_b = input(" ][ Aberto ou [] Fechado: ")
    if a_b.lower() == '][':
        if n1 < n2:
            print("]", end=" ")
            for i in range(n1 + 1, n2):
                print(f"{i} ", end="")
            print("[")
        elif n1 > n2:
            print("]", end=" ")
            for i in range(n2 + 1, n1):
                print(f"{i} ", end="")
            print("[")
        else:
            print("]",n1,"[")
    elif a_b.lower() == '[]':
        if n1 < n2:
            print("[", end =" ")
            for i in range(n1, n2 + 1):
                print(f"{i} ",end="")
                print("]")
        elif n1 > n2:
            print("[", end=" ")
            for i in range(n2, n1 + 1):
                print(f"{i} ", end="")
                print("]")
        else:
            print("[",n1,"]")




def intervalo_c_d():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if n1 < n2:
        print("[", end=" ")
        for i in range(n1, n2 + 1):
            print(f"{i} ", end="")
        print("]")

    elif n1 > n2:
        print("[", end=" ")
        for i in range(n1, n2 - 1, -1):
            print(f"{i} ", end="")
        print("]")

    else:
        print("[", n1, "]")


def invalido():
    print("Opção inválida!")


def continuar_menu():
    print(f"""
Continuar usando o menu?
(S) SIM
(N) NÃO""")

def exibir_contagem():
    print(f'''
    1 - Intervalo - {cont1}
    2 - Intervalo Aberto e Fechado - {cont2}
    3 - Intervalo em ordem crescente e decrescente - {cont3}''')

cont1 = 0
cont2 = 0
cont3 = 0


while True:
    menu()
    escolha = input("Escolha: ")
    if escolha =="1":
        intervalo()
        cont1 += 1
    elif escolha == "2":
        intervalo_a_f()
        cont2 += 1
    elif escolha == "3":
        intervalo_c_d()
        cont3 += 1
    elif escolha == "0":
        exibir_contagem()
        break
    else:
        invalido()
    continuar_menu()
    continuar = input("Digite aqui: ")
    if continuar.lower() =="n":
        exibir_contagem()
        break
    elif continuar.lower() =="s":
        continue
    else:
        invalido()
    continuar_menu()
    continuar = input("Digite aqui: ")
    if continuar.lower() == "n":
        exibir_contagem()
        break
    elif continuar.lower() == "s":
        continue
    else:
        invalido()


from triangulo import Triangulos
def main ():

    opcao = 0
    while opcao != 1:
        entrada1 = float(input("Digite o valor do primeiro lado do triangulo: "))
        entrada2 = float(input("Digite o valor do segundo lado do triangulo: "))
        entrada3 = float(input("Digite o valor do terceiro lado do triangulo: "))

        tri = Triangulos()
        print(tri.verificar(entrada1, entrada2, entrada3))

        opcao = int(input("Deseja sair: SIM(1) ou NAI(2)"))

    print("Adeus:")

if __name__ == '__main__':
    main()

''' 56. Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da 
série harmônica:
                       H(n) = 1 + 1/2 + 1/3 + 1/4 + ::: + 1=n
 Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).'''


def main():
    i = 0
    soma = 0.0
    auxiliar = 1
    while auxiliar:
        auxiliar = int(input("Digite um numero: "))
        print("\nUsuario digitou:", auxiliar, "\n")
        soma = 0.0
        if auxiliar:
            for i in range(1, auxiliar + 1):
                soma += 1.0 / i
            print("\nO resultado da serie é: ", soma, "\n")
        else:
            print("\nentrada terminada pelo usuario\n")

if __name__ == '__main__':
    main()

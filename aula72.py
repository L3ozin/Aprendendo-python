# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplica(1, 2, 3, 4, 5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

numero = int(input("Digite um numero: "))


def paridade(numero):

    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    else:
        print(f"O numero {numero} é impar")


paridade(numero)

"""Calculadora com while"""

while True:

    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operacao = input("+, -, *, /: ")

    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)

    if operacao == "+":
        print(numero_1_float + numero_2_float)
    elif operacao == "-":
        print(numero_1_float - numero_2_float)
    elif operacao == "*":
        print(numero_1_float * numero_2_float)
    elif operacao == "/":
        print(numero_1_float / numero_2_float)

    sair = input("Quer sair? [s] ").lower().startswith("s")

    if sair == True:
        break


""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
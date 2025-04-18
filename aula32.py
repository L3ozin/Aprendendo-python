"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input("Digite um numero inteiro: ")

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f"{numero_int} é par")
    else:
        print(f"{numero_int} é ímpar")
except:
    print("Isso nao é um numero inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input("Que horas é agora? ")

try:
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <= 11:
        print("Bom dia!")
    elif horas_int >= 12 and horas_int <= 17:
        print("Boa tarde!")
    elif horas_int >= 18 and horas_int <= 23:
        print("Boa noite!")
except:
    print("Isso nao é um numero inteiro!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("Qual o seu primeiro nome? ")

try:
    if len(primeiro_nome) <= 4:
        print("Seu nome é curto")
    elif len(primeiro_nome) <= 6:
        print("Seu nome é normal")
    elif len(primeiro_nome) > 6:
        print("Seu nome é muito grande")
except:
    print("Algo deu errado!")

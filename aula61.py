"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""
import re
import sys

cpf = '74682489070'

soma = 0
multiplicador = 10

cpf_limpo = re.sub(
    r'[^0-9]',
    '',
    cpf
)

entrada_e_sequencial = cpf == cpf[0] * len(cpf)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()    
    
    # primeiro digito
for primeiro_digito in cpf_limpo[:-2]:
    soma += int(primeiro_digito) * multiplicador
    multiplicador -= 1
    
primeiro_digito = (soma * 10) % 11
    
if primeiro_digito >= 9:
    resultado = 0
else:
    resultado_primeiro = primeiro_digito
    
        
    # segundo digito
soma = 0
multiplicador = 11
    
for segundo_digito in cpf_limpo[:-1]:
    soma += int(segundo_digito) * multiplicador
    multiplicador -= 1

segundo_digito = (soma * 10) % 11
    
if segundo_digito >= 9:
    resultado = 0
else:
    resultado_segundo = segundo_digito
        
cpf_gerado_pelo_calculo = f'{cpf_limpo[:-2]}{resultado_primeiro}{resultado_segundo}'



if cpf_gerado_pelo_calculo == cpf:
    print(f'O CPF :{cpf_gerado_pelo_calculo} é válido')
else:
    print('CPF Invalido')

    
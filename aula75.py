# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplica = multiplicacao(2)
triplica = multiplicacao(3)
quadruplica = multiplicacao(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))


# def duplica(n):
#     return n * 2


# def triplica(n):
#     return n * 3


# def quadruplica(n):
#     return n * 4


# print(duplica(2))
# print(triplica(2))
# print(quadruplica(2))

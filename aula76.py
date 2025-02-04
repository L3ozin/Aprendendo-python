"""        
Dicionarios em python (tipo dict)
DIcionarios são estruturas de dados do tipo
par de 'chave' e 'valor'.
Chaves podem ser consideradas com um 'indice'
que vimos na lista e podem ser de tipos imutáveis
(qualquer tipo: str, int, float, bool, tuple, etc)
E valores podem ser de qualquer tipo, incluindo
outros dicionários.
Usamos chaves - {} - ou a classe dict() para criar dicionários.
Imutaveis: str, int, float, bool, tuple
Mutaveis: dict, list
"""

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda', idade=28, altura=1.8)

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 28,
#     'altura': 1.8,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 321}
#     ]
# }

# print(pessoa, type(pessoa))

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])

"""   
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

"""
import copy

d1 = {"c1": 1, 
      "c2": 2,
      "l1": [0, 1, 2],
      }

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)

# ----------------------------------------------------------------

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)
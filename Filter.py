"""
Filter -> serve para filtrar dados de uma determinada coleção. 

filter()

valores = (1, 2, 3, 4, 5, 6)

media = (sum(valores) / len(valores))

print(media)

----------------------------------------------------------------------------------------

#Biblioteca para trabalhar com dados estatisticos

import statistics

# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'A média dos dados é: {media}')

#OBS: Assim como a função map(), a filter() recebe os parametros, sendo uma função de um interável

acima_media = filter(lambda acima: acima > media, dados)

abaixo_media = filter(lambda abaixo: abaixo < media, dados)

print(f'Os valores acima da média são: {list(acima_media)}')
print(f'Novamente: {list(acima_media)}')

print(f'Os valores abaixo da média são: {list(abaixo_media)}')
print(f'Novamente: {list(abaixo_media)}')

#OBS: assim como na função map(), após o uso dos dados de filter os mesmos são excluídos após 3 segundos da memória.

---------------------------------------------------------------------------------------------------------------------

# uma outra função bem interessante do filter() é a remoção de dados que estão faltando ou nulos

paises = ['', 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Equador', '', '', 'Uruguai']

print('Lista de paises sem aplicação do filtro para dados NULOS')

print(paises)

paises_nao_nulos = filter(None, paises)   #A função None filtra os campos vazios em uma coleção de dados
print()

print(f' Lista de paises após a aplicação do filtro: {list(paises_nao_nulos)}')

"""

#EX_02

paises = ['', 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Equador', '', '', 'Uruguai']

print(paises)

#OUtra forma de fazer com uso do lambda

paises_nao_nulos = filter(lambda pais: pais != '', paises)
print()
print(f' Lista de paises após a aplicação do filtro: {list(paises_nao_nulos)}')



 
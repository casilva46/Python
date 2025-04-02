


from collections import Counter

# Exemplo

texto = """ A Wikipédia é um projeto de enciclopédia multilíngue de licença livre,[2][3] baseado na web e escrito de maneira colaborativa.
[3] Foi lançado em 2001 por Jimmy Wales e Larry Sanger[4] e é atualmente administrado pela Fundação Wikimedia[5] (organização sem fins 
lucrativos que engaja pessoas para desenvolver conteúdo educacional sob uma licença livre ou no domínio público e para disseminá-lo globalmente),
[6] integrando vários projetos[2] mantidos pela fundação. É formada por mais de 61 milhões de artigos (1 119 168 em português, até 19 de 
fevereiro de 2024) escritos de forma conjunta por diversos editores voluntários ao redor do mundo. Em maio de 2023, havia edições ativas da 
Wikipédia em 321 idiomas.

Quase todos os verbetes presentes no sítio eletrônico podem igualmente ser editados por qualquer pessoa com acesso à internet e que possua 
um endereço eletrônico.[nota 2] Esta enciclopédia tornou-se a maior e mais popular obra de referência geral na internet.[7][8] Em 2010, 
tinha cerca de 365 milhões de leitores.[9] A Wikipédia é uma ferramenta de pesquisa amplamente utilizada por estudantes e tem influenciado o 
trabalho de publicitários, pedagogos, sociólogos e jornalistas, que usam seu material, mesmo que nem sempre citem suas fontes.[10]"""

palavras = texto.split()
print(palavras)

resultado_contador = Counter(palavras)
print(resultado_contador)

#Encontrando as 10 palavras com mais ocorrencias no texto.

print(resultado_contador.most_common(10))
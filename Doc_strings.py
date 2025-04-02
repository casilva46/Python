"""
Documentando funções com Docstrings (comentários escritos para entender o código)

print(help(print))    #solicitando ajuda a respeito de uma função em python

Podemos ter acesso a documentação em python utilizando a propriedade especial print(diz_oi.__doc__)

"""
#EX

def diz_oi():
    """Uma função simples que retorna a string oi"""
    return "oi!"

print(diz_oi())

print(help(diz_oi))

print(diz_oi.__doc__)





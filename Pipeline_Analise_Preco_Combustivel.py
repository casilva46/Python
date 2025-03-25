import wget
import zipfile
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

pd.set_option("display.max_rows", 1000)


#Faz o Download do arquivo 

url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2024-01.zip'
 
file_Path = 'Download_anl_comb_1_2024.zip'

wget.download(url, file_Path)

print()
print('download terminado')
print()
print('=============================================================================================================================================================')



## extração do arquivo Download_anl_comb_1_2024.zip

def main():
    
    # Atribuindo o nome do arquivo a uma variável
    file_name = 'Download_anl_comb_1_2024.zip' 
    
    # Abrindo o arquivo ZIP usando 'with' em modo de leitura
    with zipfile.ZipFile(file_name, 'r') as Anl_comb_1_2024: 
        
        # printing all the information of archive file contents using 'printdir' method
        print(Anl_comb_1_2024.printdir())

        # Extrai todos os arquivos utilizando o método extracall()
        print('Extraindo todos os arquivos ...')
        Anl_comb_1_2024.extractall()
        
        # check your directory of zip file to see the extracted files
        print('Extração de arquivo Finalizada!')

if __name__ == '__main__': main()
print('=============================================================================================================================================================')

df = pd.read_csv('Preços semestrais - AUTOMOTIVOS_2024.01.csv', encoding= 'ISO-8859-1', sep= ';')
print()
print('Obtendo informações do tipo de arquivo')
print()
df.info()
print()
print('=============================================================================================================================================================')

print(df)

# A partir desse ponto começa o tratamento dos dados contidos no DataFrame. Observe que no campo Valor de venda está com virgula e isso para o Python é um problema, pois não permite certos tipos de iterações. A solução é trocar as virgulas por pontos. 

print('Substuindo as virgulas por pontos')
print()

#def remove_virgula(x):
#    try:
#        x = str(x).replace(',', '.')
#        return float(x)
#    except:
#        return np.NaN
    
#df['Valor de Venda'] = df['Valor de Venda'].map(remove_virgula)

# Excluindo as colunas desnecessárias para a nossa análise

excluir_colunas = ['CNPJ da Revenda', 'Nome da Rua', 'Numero Rua', 'Complemento', 'Bairro', 'Cep', 'Valor de Compra']

df = df.drop(excluir_colunas, axis= 1)

# Exluindo uma coluna especifica

df.rename(columns={'ï»¿Regiao - Sigla': 'Regiao', 'Estado - Sigla':'Estado'}, inplace= True)

print('=============================================================================================================================================================')
print()
print('Validação se as colunas foram removidas e renomeadas')
print()
df.info()

print('=============================================================================================================================================================')
print()
print('DataFrame finalizado com os dados tratados e limpos')
print()
print(df)

print('=============================================================================================================================================================')

#Disponibilizando o arquivo tratado para os analistas

df.to_csv('Novo_dataframe_anl_comb.csv', encoding= 'ISO-8859-1', sep= ';')
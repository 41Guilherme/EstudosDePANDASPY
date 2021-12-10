import pandas as pd
from IPython.display import display

#dataframe = pd.DataFrame()

# venda = {
#         'data' : ['12/12/2021', '12/01/2022'],
#         'valor' : [500, 300],
#         'produto' : ['arroz', 'feijao'],
#         'qtde' : [50,70]
#         }

# vendas_df = pd.DataFrame(venda)

# display(vendas_df)

vendas_df1 = pd.read_excel("Vendas.xlsx")

# display(vendas_df1.head(10))   head(n) -> quantas linhas deseja ver (n)
# display(vendas_df1.shape)      shape -> retorna quantas linhas e colunas (l x c) 
# display(vendas_df1.describe()) describe()  -> retorna analise geral dos dados

produtos = vendas_df1[['Produto', 'ID Loja']] # pegando colunas e botando em produtos

linha2 = vendas_df1.loc[2] # pegando a linha 2

linha1_5 = vendas_df1[1:5] #pegando da linha 1 ate a 5

# Pegar linhas com condições

comparacao = vendas_df1['ID Loja'] == 'Norte Shopping'

vendas_norte_shopp = vendas_df1.loc[comparacao]

vendas_norte_shopp2 = vendas_df1.loc[comparacao, ['ID Loja' , 'Produto', 'Quantidade']]
# .loc(linhas , colunas)

# print(vendas_df1.loc[1,'Produto'])

# CRIAÇÃO DE COLUNA A PARTIR DE OUTRA COLUNA
vendas_df1['Comissão'] = vendas_df1['Valor Final'] * 0.2

#CRIAÇÃO DE COLUNA DO 0
vendas_df1.loc[:, "Imposto"] = 0 # Coluna Zerada


#Juntando planilhas 
vendadez_df = pd.read_excel("Vendas - Dez.xlsx")
vendas_df1 = vendas_df1.append(vendadez_df)

#Excluir
vendas_df1.drop("Imposto", axis=1) # 1 coluna / 0 Linha


#Tratamento de Valores VAZIOS
vendas_df1 = vendas_df1.dropna(how="all" , axis=1) #deleta uma linha e coluna completamente vazia
vendas_df1 = vendas_df1.dropna() #Se ao mesmo um item estiver vazio deleta
vendas_df1['Comissão'] = vendas_df1['Comissão'].fillna(0) #preenche com 0 valores vazio de uma coluna

vendas_df1['Comissão'] = vendas_df1['Comissão'].fillna(vendas_df1["Comissão"].mean()) #preenche com a media
vendas_df1 = vendas_df1.ffill() # preenche com o valor logo acima



transacoes = vendas_df1["ID Loja"].value_counts() # conta cada tipo que aparece na coluna dada
faturamento = vendas_df1[['Produto', 'Valor Final']].groupby('Produto').sum()


gerentes = pd.read_excel('Gerentes.xlsx')

vendas_df1  = vendas_df1.merge(gerentes)
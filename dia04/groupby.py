#%%

import pandas as pd 

df = pd.read_excel('../data/transactions.xlsx')
df

# %% #* Sumarizção de Dados com um unico numero

condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
df_user['Points'].sum()

# %%

pontos = {}

for i in df['IdCustomer'].unique():
    condicao = df['IdCustomer'] == i
    pontos[i] = df[condicao]['Points'].sum()

pontos

# %% #* Agrupa o DF por IdCustomer e na coluna Points vc soma os pontos de cada usuario

df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()

# %% #* df agrupado por IdCustomer, *o agg serve para fazer mais de uma operação dentro do axis!* depois pega os pontos e soma,
#* o id vai ser contado e a dt de transação pegar o mais alto,depois reseta o index epor final renomeia as colunas

(df.groupby(['IdCustomer'])
   .agg({
       'Points':'sum',
       'UUID':'count',
       'DtTransaction':'max',
        })
   .reset_index()
   .rename(columns={
           'Points':'Valor',
           'UUID':'Frequencia',
           'DtTransaction':'UltimaData'
           })
   )

#%%

import datetime

data1 = df['DtTransaction'][0]
now = datetime.datetime.now()

(now - data1).days

# %%

(datetime.datetime.now() - df['DtTransaction'][0]).days

# %% #* primeiro restringe o dataset para um usuário só, no diff pegamos a ultima data de compra e subtrai pelo horario de agora,
#* dps usamos a funcao days para ver apenas os dias.

condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]

diff = datetime.datetime.now() - df_user['DtTransaction'].max()

diff.days
# %% #* função de agregação personalizada

def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(['IdCustomer'])
   .agg({
       'Points':'sum',
       'UUID':'count',
       'DtTransaction':recencia,
        })
   .reset_index()
   .rename(columns={
           'Points':'Valor',
           'UUID':'Frequencia',
           'DtTransaction':'UltimaData'
           })
   )

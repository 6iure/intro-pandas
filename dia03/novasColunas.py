# %%

import pandas as pd 
import numpy as np 

#%%

df = pd.read_csv("../data/customers.csv", p=";")
df

# %%

df['DoublePoints'] = df['Points'] * 2
df

# %%

df['PointsRatio'] = df['DoublePoints'] / df['Points']
df

# %%

df['Constant'] = 1
df

# %%

df['PointsLog'] = np.log(df['Points'])
df

# %%

np.log(df[['Points', 'DoublePoints', 'PointsRatio']])

# %%

nomes_alta = []

for i in df['Name']:
    nomes_alta.append(i.upper())

df["NomeAlta"] = nomes_alta
df

# %%

df["Name"].str.upper()

# %% #* tentando pegar apenas o primeiro nome de um nome que tem underline e colocando em caixa alta

def get_first(nome:str):
    nome = nome.upper()
    return nome.split('_')[0]

# %%

df["FirstName"] = df['Name'].apply(get_first)
df

# %% #! lambda é uma forma de definir uma função bem simples.

getF = lambda nome: nome.split('_')[0]
getF('Téo_Calvo') 

# %%

df['Name'].apply( lambda x: x.upper().split('_')[0] )

# %%

def intervaloPontos(pontos):
    if pontos < 2500:
        return 'baixo'
    elif pontos < 3500:
        return 'médio'
    else:
        return 'alto'
    
df['FaixaPontos'] = df['Points'].apply(intervaloPontos)
df

# %%

df['UUID'].apply(lambda x: x[-3:])

# %%

df


# %%

data = {
    'nome': ['teo', 'nah', 'maria', 'lara'],
    'recencia': [1,30,10,45],
    'valor': [100,2000,15,500],
    'frequencia': [2,5,1,15]
}

df_crm = pd.DataFrame(data)
df_crm

def rfv(row):

    nota = 0

    if row['recencia'] <= 10:
        nota += 10

    elif 10 < row['recencia'] <= 30:
        nota += 5

    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10

    if 100 <= row['valor'] < 1000:
        nota += 5
    
    if row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10

    elif 5 <= row['frequencia'] < 10:
        nota += 5

    elif row['frequencia'] < 5:
        nota += 0

    return nota

# %%
df_crm['RFV'] = df_crm.apply(rfv, axis=1)
df_crm
# %%

df_crm.iloc[0]
# %%

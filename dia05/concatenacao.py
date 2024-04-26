#%%

import pandas as pd
import os 

df_1 = pd.read_csv('../data/ipea/homicidios.csv', sep=';')
df_1 = df_1.rename(columns={'valor':'homicidios'})
df_1

# %%

df_2 = pd.read_csv('../data/ipea/homicidios-por-armas-de-fogo.csv', sep=';')
df_2 = df_2.rename(columns={'valor':'homicidios_por_armas_de_fogo'})
df_2

# %%

df_1 = df_1.set_index(['cod', 'nome', 'período'])
df_2 = df_2.set_index(['cod', 'nome', 'período'])
df_2
# %%

df_2

# %% com o axis=1, empilhamos a lista verticalmente

pd.concat([ df_1, df_2, ], axis=1).reset_index()

#%% #! Função para importar caminho dos dataframes

def import_etl(path:str):

    name = path.split("/")[-1].split(".")[0]

    df = (pd.read_csv(path, sep=';')
            .rename(columns={'valor':name})
            .set_index(['cod', 'nome', 'período']))
    
    return df
# %%

path = '../data/ipea/'
files = os.listdir(path)

#%%

dfs = []
for i in files:
    dfs.append(import_etl(path+i))

# %%

df_bia = pd.concat(dfs, axis=1).reset_index()
df_bia.to_csv('../data/bia_consolidado.csv', sep=';', index=False)
df_bia

# %%

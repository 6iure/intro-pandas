# %%

import pandas as pd
import numpy as np

data = {
    'nome':['Téo', 'Nah', 'Lah', 'Maria', 'Jo'],
    'idade':[31,32,34,12,np.nan],
    'renda':[np.nan,3245,357,12432,np.nan]
}

df = pd.DataFrame(data)
df

# %%

df['idade'].isna().sum()

# %%

df.isna().sum()

# %% #* calculando a proporção de registros faltantes por coluna

df.isna().mean()

# %% #* preenchendo os valores nulos com a média de cada coluna

df.fillna({'idade': df['idade'].mean(),
           'renda': df['renda'].mean(),
           })

# %%

df.dropna(subset=['idade', 'renda'], how='all')

# %%

df.dropna(axis=1, thresh=4 )

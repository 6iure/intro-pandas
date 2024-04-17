# %%
import pandas as pd

# %%

idades = [30, 42, 90, 31]
idades

# %%

medias = sum(idades) / len(idades)

total = 0 
for i in idades:
    total += (medias -i)**2

variancia = total / (len(idades) - 1)
variancia

# %%

series_idades = pd.Series(idades)
series_idades

# %%
series_idades.mean()
# %%
series_idades.var()
series_idades.std()
# %%
series_idades.median()

# %%
series_idades.quantile(0.25)
# %%
series_idades.describe()
# %%

## o shape dirá quantas linhas sua série tem
series_idades.shape

# %%

series_idades[3]
# %%
series_idades.index = ['t', 'e', 'o', 'c']
series_idades['t']
# %%

series_idades[3]

# %%

series_idades.index = [40, 10, 30, 20]
series_idades

# %%
#! independemente do índice, vai buscar pela POSIÇÃO dos elementos.
series_idades.iloc[0]

# %%
#! já o LOC é busca pelo VALOR atrelado para o índice    
series_idades.loc[30]
# %%
series_idades.iloc[0:2]

# %%

series_idades.name = 'idades'
series_idades
# %%

series_idades = pd.Series(idades, name="TESTE")
series_idades
# %%

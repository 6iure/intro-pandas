# %% 
import pandas as pd
# %%

dados = {

    "nome":["Téo", "Nah", "Napoleão"],
    "idade": [31, 32, 14]
}

# %%

df = pd.DataFrame(dados)
df

# %% 

df.describe()

# %%
dados_idade = df['idade'] 
dados_idade
# %%

dados_idade.mean()
# %%

df['nome'].iloc[2]
# %%
df['nome'][2]

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

sumario_numericas = df.describe()
sumario_numericas

# %%

df['nome'].describe()

# %%
dados_idade = df['idade'] 
dados_idade
# %%

dados_idade.mean()
# %%

df['nome'].iloc[2]
# %%
df['nome'][2]

# %%

df['nome'].iloc[-1]
# %%

import pandas as pd
# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
#! ORDENando os pontos e os nomes.

df.sort_values().tail(10)

# %% #! o padrão é do menor para o maior

df.sort_values(by="Points", ascending=False, inplace=True)
df.rename(columns={"Name":"Nome", "Points":"Pontos"}, inplace=True)

# %%

df

# %%

df = (df.sort_values(by=["Points", "Name"],
                    ascending=[False, True])
      .rename(columns={"Name":"Nome", "Points":"Pontos"}))

df
# %%


#%%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")

df

# %% quer saber o valor da ultima transacao de cada id customer 

df_last = (df.sort_values("DtTransaction", ascending=False)
 .drop_duplicates(subset=['IdCustomer'], keep="first"))

# %%
df_last['IdCustomer'].nunique()

# %%

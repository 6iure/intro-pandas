# %% 

import pandas as pd
# %%

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
dados
# %%

dados_num = pd.Series(dados)
# %%
dados_num
# %%

dados_num.mean()
# %%

dados_num.std()

# %%
dados_num.max()

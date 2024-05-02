# %%

import pandas as pd

df = pd.read_csv('../data/bia_consolidado.csv', sep=';')
df

# %%

df = df.set_index(['cod', 'nome', 'período'])

# %%

df_stack = df.stack().reset_index()

# %%

df_stack.rename(columns={'level_3':'Tipo de Homicídio',
                   0:'Qtde'}, inplace=True)

df_stack

# %%

df_unstack = (df_stack.set_index(['cod', 'nome', 'período', 'Tipo de Homicídio'])
 .unstack()
 .reset_index()
 )

# %%

homicidios = df_unstack['Qtde'].columns.tolist()
homicidios
# %%

df_unstack.columns = ['cod', 'nome', 'período'] + homicidios
df_unstack

# %%

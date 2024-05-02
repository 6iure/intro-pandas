#%%

import pandas as pd
import numpy as np

df = pd.read_excel('../data/transacao_cartao.xlsx')
df

# %%

df['ValorParcela'] = df['Valor'] / df['Parcelas']
df 

# %% #! criando lista de quanto custa exatemente cada parcela

df['ValorParcela'] = df.apply(lambda row: [row['Valor'] / row['Parcelas'] for i in range(row['Parcelas'])], axis=1)
df

# %%

df_fatura = df.explode('ValorParcela')
df_fatura

#%%

df_fatura = df_fatura.drop(['Valor', 'Parcelas'], axis=1)
df_fatura

# %%

df_fatura['added_months'] = (df_fatura.groupby('idTransaction')['dtTransaction'].rank('first').astype(int))
df_fatura

# %%

def added_months(row):
    new_date = row['dtTransaction'] + np.timedelta64(row['added_months'], 'M')
    dt_str = f"{new_date.year}-{new_date.month:02}"
    return dt_str

df_fatura['dtFatura'] = df_fatura.apply(added_months, axis=1)
df_fatura

# %% #! mostra quanto o cliente tem q pagar em cada um dos meses

df_fatura_mes = df_fatura.groupby(['idCliente', 'dtFatura'])['ValorParcela'].sum()
df_fatura_mes = df_fatura_mes.reset_index()
df_fatura_mes

# %%

df_fatura_mes = df_fatura_mes.pivot_table(columns='dtFatura', index='idCliente', values='ValorParcela')
df_fatura_mes = df_fatura_mes.fillna(0)
df_fatura_mes

# %%

df_fatura_mes.to_excel('fatura_detalhada.xlsx')

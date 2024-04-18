# %% 

import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %%

df_customers.shape

# %%

df_customers.info(memory_usage='deep')
# %%

df_customers["Points"].astype(int)

# %%

df_customers["Points"].describe()

# %%

condicao = df_customers['Points'] > 1000


#* retornará as linhas que são true do valor booleano
df_customers[condicao]
# %%

notas = [4, 5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)

        
# %%
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas

# %%

maximo = df_customers["Points"].max()
maximo
# %%
condicao = df_customers["Points"] == maximo
condicao
# %%

df_customers[condicao]

# %% #! OU 

df_customers[df_customers['Points'] == df_customers["Points"].max()]['Name'].iloc[0]

# %% #! OU

condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000 )
condicao
# %%
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000


# %%

a = [1,2,3,4]
b = a
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %%

df_customers[['UUID', 'Name']]

# %%


colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers

# %% renomeando colunas, porem o rename cria um df novo com novos nomes nas colunas, temos que reatribuir o df

df_customers = df_customers.rename(columns={"Name": "Nome",
                              "Points" : "Pontos"})

df_customers

# %% #! o INPLACE faz a troca de nome da coluna já no msm df, ou seja n precisa de retribuição!

df_customers.rename(columns={"Id":"ID"}, inplace=True)
df_customers

# %%



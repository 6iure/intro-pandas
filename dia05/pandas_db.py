#%%

import pandas as pd
import sqlalchemy

# %% #! necessariamente aspas duplas 


engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
engine

# %%

df = pd.read_sql_table("transactions_cart", engine)
df

# %%

query = "SELECT * FROM customers LIMIT 10"
df_customers = pd.read_sql_query(query, engine)
df_customers

# %% #* como se fosse o db_raw do laravel kkkk...

query = ''' 
SELECT *
FROM customers as t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10'''

df_join = pd.read_sql_query(query, engine)
df_join

# %%

data_01 = {
    'id' : [1,2,3,4],
    'nome' : ['Téo', 'Mat', 'Nah', 'Mah'],
    'idade' : [31,32,32,32],
}

df_01 = pd.DataFrame(data_01)

data_02 = {
    'id' : [5,6,7,8],
    'nome' : ['José', 'Nathan', 'Arnaldo', 'Mario'],
    'idade' : [22,33,19,21],
}

df_02 = pd.DataFrame(data_02)

# %% enviando um dataframe para o banco de dados como uma tabela

df_01.to_sql('tb_fodase', engine, index=False)

# %%

df_02.to_sql('tb_fodase', engine, index=False, if_exists='replace')

# %% #?detnro do terminal do sqlite3 da pra se usar o .tables para mostrar todas as tabelas
#? e o .schema para mostrar os campos de cada tabela

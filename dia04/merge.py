#%%

import pandas as pd 

data_users = {
    'id' : [1,2,3,4],
    'nome' : ['Téo', 'Mat', 'Nah', 'Mah'],
    'idade' : [31,32,32,32],
}

df_user = pd.DataFrame(data_users)
df_user

# %%

data_transacoes = {
    'id_user' : [1,1,1,2,3,3,5],
    'v1' : [432,532, 123, 6,4,87,10],
    'qtProdutos' : [2,1,3,6,10,2,7],
}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao

# %%

#* SELECT * 
#* FROM df_transacao
#* LEFT JOIN df_user
#* ON df_transacao.id_user = df_user.id 

df_transacao.merge(df_user,
                      how='left', #* manter o left como referencia
                      left_on='id_user', #*chave que vou usar na base da esquerda pra 'mergar' 
                      right_on="id" #*chave que vou usar na base da direita pra 'mergar'
                      )


# %%
df_transacao.merge(df_user,
                      how='inner', #* trara apenas os usuarios que compraram e tem cadastro (intersecção)
                      left_on='id_user', #*chave que vou usar na base da esquerda pra 'mergar' 
                      right_on="id" #*chave que vou usar na base da direita pra 'mergar'
                      )

# %% #* filtro para pegar os sem cadastro

df_merge = df_transacao.merge(df_user,
                      how='left', #* manter o left como referencia
                      left_on='id_user', #*chave que vou usar na base da esquerda pra 'mergar' 
                      right_on="id" #*chave que vou usar na base da direita pra 'mergar'
                      )

df_merge[df_merge['nome'].isna()]
# %%

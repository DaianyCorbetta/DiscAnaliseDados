#
## > ATAL

# %%
# importacao de bibliotecas
import pandas as pd

# %%
#importando CSV
# Caminho dos arquivos (ajuste conforme necessário)
#alterado com Ctrl + Shift + L todos "\" por "/"
shootouts_path = 'C:/Users/User/OneDrive/Codigos_VsCOde_Pessoal/Disciplina_Analise_de_dados_2024/shootouts.csv'
results_path = 'C:/Users/User/OneDrive/Codigos_VsCOde_Pessoal/Disciplina_Analise_de_dados_2024/results.csv'
goalscorers_path = 'C:/Users/User/OneDrive/Codigos_VsCOde_Pessoal/Disciplina_Analise_de_dados_2024/goalscorers.csv'

# %%
#feito para todos csv, a fim de vertificar se carregoi certo
print(goalscorers_path)


# %%
# Importando os datasets
shootouts_df = pd.read_csv(shootouts_path, sep=',')
results_df = pd.read_csv(results_path, sep=',')
goalscorers_df = pd.read_csv(goalscorers_path, sep=',')

# Exibindo as primeiras linhas de cada dataframe
print("Shootouts- PENALTIS - Dataset:")
display(shootouts_df.head())

print("results Dataset:")
display(results_df.head())

print("goalscorers Dataset:")
display(goalscorers_df.head())


# %%
#-----------------------------------------------------------------------
######### pergunta 1
#----------------------------------------------------------------------
# Filtragem dos jogos que aconteceram em 2015 na Itália na cidade de La Spezia
# Filtrando pelo país, ano e cidade
jogos_italia_2015 = results_df[(results_df['date'].str.contains('2015')) & 
                               (results_df['country'] == 'Italy') & 
                               (results_df['city'] == 'La Spezia')]
print("jogos_italia - 2015")
display(jogos_italia_2015.head(3))

# Exibindo as colunas que quero: data, torneio e resultado
# Para o resultado, vou juntar as colunas 'home_score' e 'away_score'
jogos_italia_2015_selecionados = jogos_italia_2015[['date', 'tournament', 'home_team', 'away_team', 'home_score', 'away_score']]



# %%
# Exibir as informações dos jogos encontrados
print("Jogos em La Spezia, Itália, em 2015 foram:")
display(jogos_italia_2015_selecionados.head(3))


# %%
#-----------------------------------------------------------------------
######### pergunta 2
# 2. Qual foi a quantidade de jogos realizados no Brasil? 
# E qual foi o número de cidades que receberam estes jogos?
#----------------------------------------------------------------------

# Filtrando os jogos que ocorreram no Brasil
jogos_brasil = results_df[results_df['country'] == 'Brazil']
print(jogos_brasil)

# %%

# Contando o número total de jogos no Brasil
quantidade_jogos_brasil = len(jogos_brasil)

# Contando o número de cidades únicas que receberam os jogos no Brasil
cidades_unicas_brasil = jogos_brasil['city'].nunique()

# Exibindo os resultados
print(f"Quantidade de jogos realizados no Brasil: {quantidade_jogos_brasil}")
print(f"Número de cidades que receberam jogos no Brasil: {cidades_unicas_brasil}")


# %%
# Imprimindo cada cidade em uma linha separada
cidades_unicas_brasil_tex = jogos_brasil['city'].astype(str).unique()
print("Cidades únicas que receberam jogos no Brasil:")
for city in cidades_unicas_brasil_tex:
    print(f"- {city}")


# %%

#-----------------------------------------------------------------------
######### pergunta 3
# Jogando em casa, quantos jogos o Brasil acumulou? 
# Quantos gols em média o Brasil marcou por jogos?
#----------------------------------------------------------------------

jogos_brasil_casa = results_df[(results_df['home_team'] == 'Brazil') & 
                                (results_df['country'] == 'Brazil')]
print("jogos_brasil_casa")

# Contar o número de jogos em que o Brasil jogou em casa
quantidade_jogos_brasil_casa = len(jogos_brasil_casa)
print(quantidade_jogos_brasil_casa)

# Calcular a média de gols que o Brasil marcou jogando em casa
media_gols_brasil_casa = jogos_brasil_casa['home_score'].mean()

# Exibir os resultados
print(f"Quantidade de jogos que o Brasil jogou em casa: {quantidade_jogos_brasil_casa}")
print(f"Média de gols do Brasil jogando em casa: {media_gols_brasil_casa:.2f}")

# %%


#-----------------------------------------------------------------------
######### pergunta 4
# Qual foi a quantidade de jogos realizados na Albania, United States e Zambia, respectivamente? 
# Especificamente na Albania, em quantas cidades os jogos foram realizados e as respectivas cidades?
#----------------------------------------------------------------------

# Filtrando os jogos que ocorreram na Albânia, Estados Unidos e Zâmbia
jogos_albania = results_df[results_df['country'] == 'Albania']
jogos_us = results_df[results_df['country'] == 'United States']
jogos_zambia = results_df[results_df['country'] == 'Zambia']

# Contando o número total de jogos em cada país
quantidade_jogos_albania = len(jogos_albania)
quantidade_jogos_us = len(jogos_us)
quantidade_jogos_zambia = len(jogos_zambia)


# Exibindo os resultados
print(f"Quantidade de jogos realizados na Albânia: {quantidade_jogos_albania}")
print(f"Quantidade de jogos realizados nos Estados Unidos: {quantidade_jogos_us}")
print(f"Quantidade de jogos realizados na Zâmbia: {quantidade_jogos_zambia}")

# %%
# Listando as cidades únicas onde os jogos ocorreram na Albânia
cidades_unicas_albania = jogos_albania['city'].unique()
print(f"cidades únicas onde os jogos ocorreram na Albânia: {cidades_unicas_albania}")
# %%
quantidade_jogos_albania_unico = len(cidades_unicas_albania)
print(quantidade_jogos_albania)

#NAO FUNCIONA, RETORNA NUMERO DE VEZES QUE APRECE

# %%
print(f"\nNa Albânia, os jogos foram realizados em {len(cidades_unicas_albania)} cidades:")
for cidade in cidades_unicas_albania:
    print(cidade)

# %%
#-----------------------------------------------------------------------
######### pergunta 5
# Considerando o ano de 2016, quais cidades sediaram jogos no Brasil? 
# E quantos jogos cada cidade sediou?
#----------------------------------------------------------------------
# Filtrar os jogos realizados no Brasil em 2016
jogos_brasil_2016 = results_df[(results_df['country'] == 'Brazil') & (results_df['date'].str.contains('2016'))]
print(jogos_brasil_2016)


# %%

# Contar o número de jogos por cidade
jogos_por_cidade_2016 = jogos_brasil_2016['city'].value_counts()
#--- conta quantas vezes cada cidade aparece no filtro aplicado

# Exibir as cidades e o número de jogos que sediaram em 2016
print("Cidades que sediaram jogos no Brasil em 2016 e a quantidade de jogos:")
print(jogos_por_cidade_2016)


# %%
# %%
#-----------------------------------------------------------------------
######### pergunta 6
# Qual foi o jogo que apresentou o maior número de gols? 
# Apresente o nome dos países, campeonato, ano e número de gols.
#----------------------------------------------------------------------

# %%
# CriaÇÃO uma coluna que soma os gols do time da casa e do visitante
results_df['total_gols'] = results_df['home_score'] + results_df['away_score']

# Encontrar o índice do jogo com o maior número de gols
indice_max_gols = results_df['total_gols'].idxmax()
#---método idxmax() retorna o índice do jogo que teve o maior número de gols.

# Obter os detalhes do jogo com o maior número de gols
jogo_mais_gols = results_df.loc[indice_max_gols] 
#---loc para acessar a linha do jogo com o maior número de gols e exibimos os detalhes

# Exibir os detalhes do jogo
print(f"Jogo com o maior número de gols:")
print(f"Países: {jogo_mais_gols['home_team']} vs {jogo_mais_gols['away_team']}")
print(f"Campeonato: {jogo_mais_gols['tournament']}")
print(f"Ano: {jogo_mais_gols['date'][:4]}")  # Pega o ano da data
print(f"Número total de gols: {jogo_mais_gols['total_gols']}")

# %%
# %%
#-----------------------------------------------------------------------
######### pergunta 7
# Qual foi a cidade e o país que sediaram o maior número de partidas? 
# Quantas partidas foram realizadas?
#----------------------------------------------------------------------
# Agrupar os dados por cidade e país, contando o número de partidas
partidas_por_cidade_pais = results_df.groupby(['city', 'country']).size().reset_index(name='num_partidas')
#--- groupby() para agrupar os dados pelas colunas de cidade (city) e país (country). 
#--- size() conta o número de ocorrências para cada grupo (número de partidas em cada cidade e país).

# Encontrar o índice da cidade e país com o maior número de partidas
indice_max_partidas = partidas_por_cidade_pais['num_partidas'].idxmax()

# Obter os detalhes da cidade e país com o maior número de partidas
cidade_pais_mais_partidas = partidas_por_cidade_pais.loc[indice_max_partidas]

# Exibir os detalhes
print(f"Cidade com maior número de partidas: {cidade_pais_mais_partidas['city']}")
print(f"País: {cidade_pais_mais_partidas['country']}")
print(f"Número de partidas realizadas: {cidade_pais_mais_partidas['num_partidas']}")

# %%


# %%
# %%
#-----------------------------------------------------------------------
######### pergunta 8
# Qual foi a data do último jogo registrado no dataset? 
# Apresente a data, torneio e cidade onde este jogo foi realizado.
#----------------------------------------------------------------------

# Ordenar o dataset pela coluna 'date' em ordem decrescente
jogo_mais_recente = results_df.sort_values(by='date', ascending=False).iloc[0]
#--- sort_values(by='date', ascending=False) para ordenar o dataset pela coluna de data (date) em ordem decrescente.
#--- iloc[0] para acessar a primeira linha do dataset ordenado, que corresponde ao último jogo registrado.


# Exibir os detalhes do último jogo
print(f"Data do último jogo registrado: {jogo_mais_recente['date']}")
print(f"Torneio: {jogo_mais_recente['tournament']}")
print(f"Cidade: {jogo_mais_recente['city']}")
# %%



# %%


# %%


# %%



# %%


# %%


# %%


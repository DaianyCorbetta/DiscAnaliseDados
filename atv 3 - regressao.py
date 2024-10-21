#suponha que você esteja trabalhando em um projeto para prever o preço de carros
#  com base em suas características. Você possui um conjunto de dados com 
# informações sobre carros, incluindo várias características como potência do 
# motor, peso, consumo de combustível, entre outras. Seu objetivo é criar um 
# modelo de regressão linear simples para prever os preços dos carros com base 
# em uma única característica: a potência do motor (em cavalos-vapor, HP). 
# Além disso, você deseja visualizar os dados e a linha de regressão resultante.
#

​#Passo 1: Criar um Conjunto de Dados
#Passo 2: Visualização da Dispersão dos Dados
#​Passo 3: Ajustar um Modelo de Regressão Linear
#Passo 4: Visualizar a Linha de Regressão

# %%
​import numpy as np
#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# %%
# Passo 1: Criar um conjunto de dados fictício com 100 carros
np.random.seed(0)
potencia_motor = np.random.randint(100, 400, 100)
preco_carro = 20000 + 100 * potencia_motor + np.random.normal(0, 5000, 100)
# Crie um DataFrame do Pandas
dados_carros = pd.DataFrame({'PotenciaMotor': potencia_motor, 'Preco': preco_carro})
# Exiba as primeiras linhas do conjunto de dados
print(dados_carros.head())


# %%
# Passo 2: Criar um gráfico de dispersão
plt.scatter(dados_carros['PotenciaMotor'], dados_carros['Preco'])
plt.xlabel('Potência do Motor (HP)')
plt.ylabel('Preço do Carro')
plt.title('Relação entre Potência do Motor e Preço do Carro')
plt.show()


# %%
# Passo 3: Criar um objeto de modelo de regressão linear
modelo_regressao = LinearRegression()
# Ajustar o modelo aos dados
X = dados_carros[['PotenciaMotor']]
y = dados_carros['Preco']
modelo_regressao.fit(X, y)


# %%
# Gerar previsões com o modelo
previsoes = modelo_regressao.predict(X)


# %%
# Passo 4: Visualizar a linha de regressão
plt.scatter(dados_carros['PotenciaMotor'], dados_carros['Preco'])
plt.plot(X, previsoes, color='red', linewidth=2)
plt.xlabel('Potência do Motor (HP)')
plt.ylabel('Preço do Carro')
plt.title('Regressão Linear: Potência do Motor vs. Preço do Carro')
plt.show()


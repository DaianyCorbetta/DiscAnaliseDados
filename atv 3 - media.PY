#Pandas se integra bem com outras bibliotecas populares para ciência de dados, como 
# Matplotlib (visualização de dados), 
# NumPy (cálculos numéricos), 
# SciPy (análise científica) e 
# Scikit-Learn (aprendizado de máquina).

# --------------------------------------------------------------

#considere um conjunto de dados que representa a expressão gênica de um gene 
# específico em diferentes tecidos biológicos. 
# O DataFrame dados_gene abaixo contém esses dados, 
# onde cada linha representa um tecido e a coluna expressao_gene contém 
# os níveis de expressão desse gene em cada tecido.

#Usando o Pandas e o NumPy, calcule a média dos níveis de expressão do gene em todos os tecidos.

# %%

import pandas as pd

# %%
import numpy as np

# %%
# Criação do DataFrame
dados = { 'tecido': ['Tecido A', 'Tecido B', 'Tecido C', 'Tecido D', 'Tecido E'],
'expressao_gene': [10.2, 8.7, 12.5, 9.0, 11.8] }

dados_gene = pd.DataFrame(dados)

media_expressao = np.mean(dados_gene['expressao_gene'])

print(f"Média dos níveis de expressão do gene: {media_expressao}")
# %%

# %%

----
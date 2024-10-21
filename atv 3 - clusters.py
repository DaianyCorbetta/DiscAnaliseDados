#A clusterização é uma técnica fundamental em Ciência de Dados que envolve a 
# organização de dados em grupos ou clusters com base em suas características 
# semelhantes. Essa técnica é usada para descobrir estruturas ocultas nos dados, 
# identificar padrões naturais e agrupar pontos de dados que compartilham 
# características comuns. O principal objetivo da clusterização é dividir um 
# conjunto de dados em grupos de forma que os pontos de dados dentro de um mesmo 
# grupo sejam mais semelhantes entre si do que com os pontos em outros grupos. 
# Isso facilita a análise exploratória de dados, a segmentação de clientes, 
# a detecção de anomalias e muito mais.


#Considere um conjunto de dados de expressão gênica para agrupar genes em clusters
#  com base em seus padrões de expressão. 
# A clusterização de genes com perfis de expressão semelhantes é fundamental 
# para a análise de dados de genômica funcional.

# %%
# Importar bibliotecas
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

 # %%

# Gerar dados de expressão gênica fictícios
np.random.seed(0)
genes = ['Gene' + str(i) for i in range(1, 101)]
amostras = ['Amostra' + str(i) for i in range(1, 21)]
expressao = np.random.rand(100, 20)

# Criar um DataFrame de dados de expressão gênica
df = pd.DataFrame(expressao, columns=amostras, index=genes)

 # %%

# Aplicar o algoritmo K-Means
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
df['Cluster'] = kmeans.fit_predict(df[amostras])

# %%

# Exibir os centroides dos clusters
centroids = pd.DataFrame(kmeans.cluster_centers_, columns=amostras)
print("Centroides dos Clusters:")
print(centroids)


# %%
# Plotar os clusters de genes
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['r', 'g', 'b', 'c', 'm']
for cluster in range(n_clusters):
    cluster_genes = df[df['Cluster'] == cluster]
    ax.scatter(cluster_genes.index, cluster_genes['Amostra1'], label=f'Cluster {cluster}', c=colors[cluster])
ax.set_xlabel('Genes')
ax.set_ylabel('Expressão (Amostra 1)')
ax.set_title('Clusterização de Genes por Expressão Gênica (Amostra 1)')
ax.legend()
plt.xticks(rotation=90)

# %%
plt.show()

# %%

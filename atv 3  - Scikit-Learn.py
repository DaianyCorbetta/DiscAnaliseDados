#um modelo de classificação de diagnóstico de câncer de mama usando 
# o conjunto de dados Breast Cancer Wisconsin (Diagnosis), d
# isponível na biblioteca Scikit-Learn. 
# O objetivo é prever se um tumor é benigno (B) ou maligno (M) com base 
# em características de biópsias.

# avaliar o modelo de classificação treinado para o diagnóstico do câncer de 
# mama com base nas características das biópsias, 
 
# %%
#importar bibliotecas 
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt


# %%
# Carregar o conjunto de dados
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Categorical.from_codes(data.target, data.target_names)


# %%
# Dividir os dados em conjuntos de treinamento e teste (80% treinamento, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = clf.predict(X_test)

# %%
# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, target_names=data.target_names)
print(f'Acurácia do Modelo: {accuracy:.2f}')
print('\nMatriz de Confusão:')
print(confusion)
print('\nRelatório de Classificação:')
print(classification_rep)

# %%
# Obter as importâncias das características do modelo
feature_importances = clf.feature_importances_
indices = np.argsort(feature_importances)[::-1]

# %%

# Plotar as características mais importantes
plt.figure(figsize=(10, 6))
plt.title("Importância das Características")
plt.bar(range(X_train.shape[1]), feature_importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), X_train.columns[indices], rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.show()


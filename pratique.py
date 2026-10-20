import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head())
print(df.info())

# ------------------------------------------------------------
# 1. Histograma — distribuição do Preço
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=30, color='steelblue', alpha=0.8)
plt.title('Distribuição do Preço dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 2. Gráfico de Dispersão — Preço x Nota
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Preço', y='Nota')
plt.title('Relação entre Preço e Nota do Produto')
plt.xlabel('Preço (R$)')
plt.ylabel('Nota')
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 3. Mapa de Calor — correlação entre variáveis numéricas
# ------------------------------------------------------------
plt.figure(figsize=(12, 9))
colunas_numericas = df.select_dtypes(include='number')
sns.heatmap(colunas_numericas.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor — Correlação entre Variáveis Numéricas')
plt.show()

# ------------------------------------------------------------
# 4. Gráfico de Barras — quantidade de produtos por Marca
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
df['Marca'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Marcas com Mais Produtos')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 5. Gráfico de Pizza — proporção de produtos por Temporada
# ------------------------------------------------------------
plt.figure(figsize=(8, 8))
df['Temporada'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proporção de Produtos por Temporada')
plt.ylabel('')
plt.show()

# ------------------------------------------------------------
# 6. Gráfico de Densidade — distribuição do Desconto
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Desconto'], fill=True, color='green')
plt.title('Densidade da Distribuição de Descontos')
plt.xlabel('Desconto (%)')
plt.ylabel('Densidade')
plt.show()

# ------------------------------------------------------------
# 7. Gráfico de Regressão — N_Avaliações x Preço
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='N_Avaliações', y='Preço', scatter_kws={'alpha': 0.5})
plt.title('Relação entre Número de Avaliações e Preço (com Reta de Regressão)')
plt.xlabel('Número de Avaliações')
plt.ylabel('Preço (R$)')
plt.show()
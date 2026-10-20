import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carrega os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# ------------------------------------------------------------
# 1. Histograma — distribuição do Preço
# ------------------------------------------------------------
fig_histograma = px.histogram(
    df, x='Preço', nbins=30,
    title='Distribuição do Preço dos Produtos'
)
fig_histograma.update_layout(xaxis_title='Preço (R$)', yaxis_title='Frequência')

# ------------------------------------------------------------
# 2. Gráfico de Dispersão — Preço x Nota
# ------------------------------------------------------------
fig_dispersao = px.scatter(
    df, x='Preço', y='Nota',
    title='Relação entre Preço e Nota do Produto'
)

# ------------------------------------------------------------
# 3. Mapa de Calor — correlação entre variáveis numéricas
# ------------------------------------------------------------
colunas_numericas = df.select_dtypes(include='number')
fig_mapa_calor = px.imshow(
    colunas_numericas.corr(),
    text_auto='.2f',
    color_continuous_scale='RdBu_r',
    title='Mapa de Calor — Correlação entre Variáveis Numéricas'
)

# ------------------------------------------------------------
# 4. Gráfico de Barras — top 10 marcas com mais produtos
# ------------------------------------------------------------
top_marcas = df['Marca'].value_counts().head(10).reset_index()
top_marcas.columns = ['Marca', 'Quantidade']
fig_barras = px.bar(
    top_marcas, x='Marca', y='Quantidade',
    title='Top 10 Marcas com Mais Produtos'
)

# ------------------------------------------------------------
# 5. Gráfico de Pizza — proporção de produtos por Temporada
# ------------------------------------------------------------
temporada_counts = df['Temporada'].value_counts().reset_index()
temporada_counts.columns = ['Temporada', 'Quantidade']
fig_pizza = px.pie(
    temporada_counts, names='Temporada', values='Quantidade',
    title='Proporção de Produtos por Temporada'
)

# ------------------------------------------------------------
# 6. Gráfico de Densidade — distribuição do Desconto
# ------------------------------------------------------------
fig_densidade = px.density_contour(
    df, x='Desconto',
    title='Densidade da Distribuição de Descontos'
)
fig_densidade.update_traces(contours_coloring='fill', colorscale='Greens')

# ------------------------------------------------------------
# 7. Gráfico de Regressão — N_Avaliações x Preço
# ------------------------------------------------------------
fig_regressao = px.scatter(
    df, x='N_Avaliações', y='Preço', trendline='ols',
    title='Relação entre Número de Avaliações e Preço (com Reta de Regressão)'
)

# ------------------------------------------------------------
# Aplicação Dash
# ------------------------------------------------------------
app = Dash(__name__)
app.title = 'Análise E-commerce'

app.layout = html.Div(children=[
    html.H1('Dashboard de Análise de Dados — E-commerce', style={'textAlign': 'center'}),
    html.P(
        'Visualização interativa dos dados de produtos, preços, avaliações e descontos.',
        style={'textAlign': 'center'}
    ),

    html.H2('1. Distribuição do Preço'),
    dcc.Graph(figure=fig_histograma),

    html.H2('2. Preço x Nota'),
    dcc.Graph(figure=fig_dispersao),

    html.H2('3. Correlação entre Variáveis Numéricas'),
    dcc.Graph(figure=fig_mapa_calor),

    html.H2('4. Top 10 Marcas'),
    dcc.Graph(figure=fig_barras),

    html.H2('5. Produtos por Temporada'),
    dcc.Graph(figure=fig_pizza),

    html.H2('6. Densidade dos Descontos'),
    dcc.Graph(figure=fig_densidade),

    html.H2('7. Avaliações x Preço (Regressão)'),
    dcc.Graph(figure=fig_regressao),
])

if __name__ == '__main__':
    app.run(debug=True)
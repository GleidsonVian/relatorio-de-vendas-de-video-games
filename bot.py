import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados do CSV
dados = pd.read_csv(r'C:\Users\gleid\pasta4\Python\relatorio de vendas de video games\vendas de jogos.csv')

# Ordena os dados pela coluna 'Copies sold' em ordem decrescente
maiores_vendas = dados.sort_values(by='Copies sold', ascending=False)

# Seleciona as colunas de interesse
colunas_de_interesse = ['Game', 'Copies sold', 'Release date[a]', 'Genre(s)', 'Publisher(s)']

# Filtra os dados para incluir apenas as colunas selecionadas
dados_filtrados = maiores_vendas[colunas_de_interesse]

# Renomeia as colunas
dados_filtrados = dados_filtrados.rename(columns={
    'Game': 'Jogo',
    'Copies sold': 'Cópias Vendidas',
    'Release date[a]': 'Data de Lançamento',
    'Genre(s)': 'Gênero',
    'Publisher(s)': 'Publicadora'
})

# Exporta os dados filtrados e renomeados para um arquivo Excel
dados_filtrados.to_excel(r'C:\Users\gleid\pasta4\Python\relatorio de vendas de video games\maiores_vendas.xlsx', index=False)

# Plotando um gráfico de barras com os dados
plt.figure(figsize=(10, 6))
plt.bar(dados_filtrados['Jogo'][:10], dados_filtrados['Cópias Vendidas'][:10], color='skyblue')
plt.xlabel('Jogo')
plt.ylabel('Cópias Vendidas')
plt.title('Top 10 Jogos por Cópias Vendidas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Salvar o gráfico automaticamente
caminho_grafico = r'C:\Users\gleid\pasta4\Python\relatorio de vendas de video games\top_10_jogos_vendidos.png'
plt.savefig(caminho_grafico)

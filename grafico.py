import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
dados = pd.read_excel("assets/dados.xlsx")

# Separando as colunas
periodo = dados["Periodo"]
valor = dados["Valor"]

# Criando o gráfico
plt.figure(figsize=(12, 6)) # cria uma janela com a gráfico
# plt.plot(periodo, valor, marker="o")
# plt.bar(periodo,valor) # gráfico de barras
plt.fill_between(periodo,valor)


# Deixando as legendas do eixo X na vertical
plt.xticks(rotation=90)

# Configurações do gráfico
plt.title("Evolução dos Valores ao Longo do Tempo")
plt.xlabel("Período")
plt.ylabel("Valor")
plt.grid(axis="y")

# Ajusta automaticamente os espaços
plt.tight_layout()

# Exibindo o gráfico
plt.show()
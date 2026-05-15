import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
dados = pd.read_excel("dados.xlsx")

# Separando as colunas
periodo = dados["Periodo"]
valor = dados["Valor"]

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(periodo, valor, marker="o")


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
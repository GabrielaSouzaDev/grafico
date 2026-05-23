from ast import main
from os import link, system

import customtkinter as ctk
import matplotlib.pyplot as plt
import pandas as pd



ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
ctk.set_widget_scaling(0.5)
ctk.set_window_scaling(2.0)

app = ctk.CTk()
app.geometry('400x400')
app.title('Gerador de Gráficos')
app.iconbitmap('assets/grafico.ico')


def buscar():
    link = excelEntrada.get()
    if link:
        try:
            dados = pd.read_excel(link)
            periodo = dados["Periodo"]
            valor = dados["Valor"]
            plt.figure(figsize=(12, 6))
            plt.fill_between(periodo, valor)
            plt.xticks(rotation=90)
            plt.title("Evolução dos Valores ao Longo do Tempo")
            plt.xlabel("Período")
            plt.ylabel("Valor")
            plt.grid(axis="y")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
    else:
        print("Por favor, insira o caminho do arquivo Excel.")

def gerar_grafico():
    link = excelEntrada.get()
    if link:
        try:
            dados = pd.read_excel(link)
            periodo = dados["Periodo"]
            valor = dados["Valor"]
            plt.figure(figsize=(12, 6))
            plt.fill_between(periodo, valor)
            plt.xticks(rotation=90)
            plt.title("Evolução dos Valores ao Longo do Tempo")
            plt.xlabel("Período")
            plt.ylabel("Valor")
            plt.grid(axis="y")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
    else:
        print("Por favor, insira o caminho do arquivo Excel.")



titulo = ctk.CTkLabel(app, 
                      text='Gerador de Gráficos', 
                      font=('Arial', 50, 'bold'))
titulo.pack(pady=40)

excelEntrada = ctk.CTkEntry(app,
                            font=('Arial', 30),
                            width=500,
                            height=60,
                            placeholder_text='Digite o caminho do arquivo Excel...')
excelEntrada.pack(pady=30, padx=20)

botaoBuscar = ctk.CTkButton(app, 
                            text='Buscar Excel',
                            command=buscar,
                            corner_radius=10,
                            fg_color='#007ACC',
                            hover_color='#005A9E',
                            width=300,
                            height=60,
                            font=('Arial', 30))
botaoBuscar.pack(pady=20)

botaoGerar = ctk.CTkButton(app, 
                            text='Gerar Gráfico',
                            command=gerar_grafico,
                            corner_radius=10,
                            fg_color='#007ACC',
                            hover_color='#005A9E',
                            width=300,
                            height=60,
                            font=('Arial', 30))
botaoGerar.pack(pady=20)

app.mainloop()
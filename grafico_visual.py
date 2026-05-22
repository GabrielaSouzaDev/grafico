from ast import main
from os import system

import customtkinter as ctk
import matplotlib.pyplot as plt

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
ctk.set_widget_scaling(0.5)
ctk.set_window_scaling(2.0)

app = ctk.CTk()
app.geometry('400x400')
app.title('Gerador de Gráficos')
app.iconbitmap('assets/grafico.ico')








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
                            # command=buscar,
                            corner_radius=10,
                            fg_color='#007ACC',
                            hover_color='#005A9E',
                            width=300,
                            height=60,
                            font=('Arial', 30))
botaoBuscar.pack(pady=20)

botaoGerar = ctk.CTkButton(app, 
                            text='Gerar Gráfico',
                            # command=gerar_grafico,
                            corner_radius=10,
                            fg_color='#007ACC',
                            hover_color='#005A9E',
                            width=300,
                            height=60,
                            font=('Arial', 30))
botaoGerar.pack(pady=20)

app.mainloop()
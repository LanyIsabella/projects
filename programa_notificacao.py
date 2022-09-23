#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Importações

from tkinter import *
import requests

# ------------ CÓDIGO -------------


# API para previsão do tempo em tempo real

def clima_atual():
    api_code = "66f848c0ffe63ea565f8a080bd41a516"
    cidade = 'são paulo'
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_code}&lang=pt_br"

    requisicao = requests.get(link)
    arquivo = requisicao.json()
    clima = arquivo['weather'][0]['description']
    temperatura = arquivo['main']['temp'] - 273
    sensacao = arquivo['main']['feels_like'] - 273
    temp_min = arquivo['main']['temp_min'] -273
    temp_max = arquivo['main']['temp_max'] - 273

    texto = f'''Na cidade {cidade.title()}, o clima é: {clima.title()}
    A temperatura atual é de: {int(temperatura)}°C
    A sensação térmica atual é de: {int(sensacao)}°C
    A temperatura mínima para hoje é de: {int(temp_min)}°C
    A temperatura máxima para hoje é de: {int(temp_max)}°C'''
    
    texto_clima['text'] = texto
    
# Cotação de valores

def pegar_cotacao():
    requisicao2 = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = requisicao2.json()
    
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_euro = cotacao['EURBRL']['bid']
    cotacao_bitcoin = cotacao['BTCBRL']['bid']
    
    texto2 = f'''-- Cotação para R$ --
    
    Dolár: R${float(cotacao_dolar):.2f}
    Euro: R${float(cotacao_euro):.2f}
    Bitcoin: R${float(cotacao_bitcoin):.3f}'''
    
    texto_cotacao['text'] = texto2 
    
    
    
# Interface

janela = Tk()
janela.title('notificações')
texto_orientacao = Label(janela, text='Clique no botão para ver as notificações do dia!')
texto_orientacao.config(font=('Ivy 25', 11))
texto_orientacao.grid(column=0, row=0, pady=15, padx=15)


# Botões

# Botão do clima
botao1 = Button(janela, text="Ver clima atual", command=clima_atual)
botao1.grid(column=0, row=1, pady=10, padx=10)


# Botão da cotação
botao2 = Button(janela, text="Ver cotação atual", command=pegar_cotacao)
botao2.grid(column=0, row=5, pady=10, padx=10)

texto_clima = Label(janela, text='')
texto_clima.config(font=('Arial', 10))
texto_clima.grid(column=0, row= 2, pady=15, padx=15)

texto_cotacao = Label(janela, text='')
texto_cotacao.config(font=('Arial', 10))
texto_cotacao.grid(column=0, row=6, pady=15, padx=15)

janela.mainloop()


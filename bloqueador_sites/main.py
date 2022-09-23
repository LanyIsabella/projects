# Importações de bibliotecas - TKinter e Pillow

from tkinter import *
from tkinter import Tk, StringVar,ttk
from PIL import Image, ImageTk

# Cores
co0 = "#f0f3f5"  # Preto
co1 = "#feffff"  # branco
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # Vermelho
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul

# Criando a janela do programa

janela = Tk()
janela.title("")
janela.geometry('390x350')
janela.configure(bg=co1)
janela.resizable(width=False, height=False)

# Frames

frame_logo = Frame(janela, width=400, height=60, bg=co1, relief="flat")
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_corpo = Frame(janela, width=400, height=400, bg=co1, relief="flat")
frame_corpo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando a logo

imagem = Image.open('icon.png')
imagem = imagem.resize((45, 45))
imagem = ImageTk.PhotoImage(imagem)

l_imagem =  Label(frame_logo, height=60, image=imagem, bg=co1)
l_imagem.place(x=20, y=5)

l_logo = Label(frame_logo, text="Bloqueador de Sites", height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_logo.place(x=70, y=10)

janela.mainloop ()
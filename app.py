#importação
from tkinter import *
from pacotes import mais

#Criando uma janela
face = Tk()
#Titiulo para a janela
face.title('Minha interface')
#tamanho da janela
face.geometry("525x350")

#saudações
saudações = Label(face, text="Seja bem vindo a minha janela grafica")
#Tamanho da label
saudações.place(x=155, y=115)

#botão
saiba_mais = Button(face, text="Saiba mais", command=mais)
saiba_mais.place(x=220, y=145)

#Essa função faz a janela ficar aberta 
face.mainloop()
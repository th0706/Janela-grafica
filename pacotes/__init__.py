from tkinter import *

def mais():
    face_1 = Tk()
    face_1.title("Segunda janela")
    face_1.geometry('525x350')
    
    #informação da segunda janela
    informações = Label(face_1,text='Sou dev Matheus essa é a minha janela grafica que criei do zero')
    informações.place(x=100, y=115)
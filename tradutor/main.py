from tkinter import *
from tkinter import ttk
from funcoes import Funcoes

root = Tk()

class Aplicacao(Funcoes):
    def __init__(self):
        self.root = root
        self.palavra = ''
        self.codigo = ''
        self.tela()
        self.frames()
        self.widgets()
        root.mainloop()
    def tela(self):
        self.root.title("Tradutor")
        self.root.geometry('700x500')
        self.root.resizable(False, False)
        self.root.configure(background='#1e3743', cursor="tcross",)
    
    def frames(self):
        self.frame_1 = Frame(self.root, bg='#dfe3ee',
                             highlightbackground='#759fa6', highlightthickness=5)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bg='#dfe3ee',
                             highlightbackground='#759fa6', highlightthickness=5)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets(self):
        self.label_codigo = Label(self.frame_1, font=("Verdana", 17), text='Digite Seu Código Aqui', bg='#dfe3ee', fg="#107bd2")
        self.label_codigo.place(relx=0.3, rely=0.03)

        self.entry_codigo = Entry(self.frame_1, font=("Verdana", 17), justify=CENTER)
        self.entry_codigo.place(relx=0.25, rely=0.23, relwidth=0.5, relheight=0.2)

        self.button = Button(self.frame_1, text="Traduzir", bg="#107bd2", bd=2, fg="white", font=("Arial", 15), command=self.traduz_codigo)
        self.button.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.2)

        self.label_palavra = Label(self.frame_1, font=("Verdana", 17), text=self.palavra, bg='#dfe3ee', fg="black")
        self.label_palavra.place(relx=0.43, rely=0.8)

        self.apagar_codigo = Button(self.frame_1, text="Limpar", bg="#107bd2", bd=2, fg="white", font=("Arial", 15), command=self.apagar_codigo)
        self.apagar_codigo.place(relx=0.75, rely=0.23, relwidth=0.11, relheight=0.2)


        self.lb_palavra = Label(self.frame_2, font=("Verdana", 17), text='Digite Sua Palavra Aqui', bg='#dfe3ee', fg="#107bd2")
        self.lb_palavra.place(relx=0.3, rely=0.03)

        self.et_palavra = Entry(self.frame_2, font=("Verdana", 17), justify=CENTER)
        self.et_palavra.place(relx=0.25, rely=0.23, relwidth=0.5, relheight=0.2)

        self.bt_palavra = Button(self.frame_2, text="Traduzir", bg="#107bd2", bd=2, fg="white", font=("Arial", 15), command=self.traduz_palavra)
        self.bt_palavra.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.2)

        self.lb_codigo = Label(self.frame_2, font=("Verdana", 17), text=self.palavra, bg='#dfe3ee', fg="black")
        self.lb_codigo.place(relx=0.43, rely=0.8)

        self.apagar_palavra = Button(self.frame_2, text="Limpar", bg="#107bd2", bd=2, fg="white", font=("Arial", 15), command=self.apagar_palavra)
        self.apagar_palavra.place(relx=0.75, rely=0.23, relwidth=0.11, relheight=0.2)


Aplicacao()
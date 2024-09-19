from tkinter import *

class Funcoes:
    def dicionario_metodo(self):
        self.dicionario = {'2': 'A', '22': 'B', '222': 'C',
                        '3': 'D', '33': 'E', '333': 'F',
                        '4': 'G', '44': 'H', '444': 'I',
                        '5': 'J', '55': 'K', '555': 'L',
                        '6': 'M', '66': 'N', '666': 'O',
                        '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
                        '8': 'T', '88': 'U', '888': 'V',
                        '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z'}
        

    def traduz_codigo(self):
        self.codigo = self.entry_codigo.get()
        if self.codigo.isalpha() or '-' not in self.codigo:
            self.label_palavra.config(text="Somente números, separados com -", fg='red')
            self.label_palavra.place(relx=0.2)
        else:
            self.dicionario_metodo()
            self.codigo = self.codigo.split("-")

            for index in range(len(self.codigo)):
                for chave, value in self.dicionario.items():
                    if self.codigo[index] == chave:
                        self.codigo[index] = value
                    

            self.palavra = ''.join(self.codigo)
            self.label_palavra.config(text=self.palavra)

    def traduz_palavra(self):
        self.palavra = self.et_palavra.get()
        if not self.palavra.isalpha():
            self.lb_codigo.config(text="Apenas Letras", fg='red')
            self.lb_codigo.place(relx=0.35)
        else:
            self.dicionario_metodo()
            self.palavra = list(self.palavra.upper()) 


            for index in range(len(self.palavra)):
                for chave, value in self.dicionario.items():
                    if self.palavra[index] == value:
                        self.palavra[index] = chave


            self.codigo = '-'.join(self.palavra)
            self.lb_codigo.config(text=self.codigo)

    def apagar_codigo(self):
        self.entry_codigo.delete(0, END)
        self.label_palavra.config(text="")

    def apagar_palavra(self):
        self.et_palavra.delete(0, END)
        self.lb_codigo.config(text="")
from tkinter import Tk, Entry, Button, StringVar
class Calculadora:
    def __init__(self, telaprincipal):
        telaprincipal.title("Calculadora Simples")
        telaprincipal.geometry('357x420+0+0')
        telaprincipal.config(bg="gray")
        telaprincipal.resizable(False, False)

        self.equacao = StringVar()
        self.valor_entrada = ''
        Entry(width=17, bg='lightblue', font=('Arial Bold', 28), textvariable=self.equacao).place(x=0, y=0)

        Button(width=11,height=4, text=')', relief='flat', bg='white', command=lambda: self.mostrar(')')).place(x=90,y=50)
        Button(width=11,height=4, text='%', relief='flat', bg='white', command=lambda: self.mostrar('%')).place(x=180,y=50)
        Button(width=11,height=4, text='1', relief='flat', bg='white', command=lambda: self.mostrar(1)).place(x=0,y=125)
        Button(width=11,height=4, text='2', relief='flat', bg='white', command=lambda: self.mostrar(2)).place(x=90,y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.mostrar(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.mostrar(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.mostrar(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.mostrar(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.mostrar(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.mostrar(8)).place(x=90, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.mostrar(9)).place(x=180, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.mostrar(0)).place(x=90, y=350)
        Button(width=11, height=4, text='X', relief='flat', bg='white', command=lambda: self.mostrar('*')).place(x=270, y=125)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.mostrar('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.mostrar('+')).place(x=270, y=200)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.mostrar('-')).place(x=270, y=275)
        Button(width=11, height=4, text='÷', relief='flat', bg='white', command=lambda: self.mostrar('/')).place(x=270, y=50)
        Button(width=11, height=4, text='=', relief='flat', bg='white', command=lambda: self.resolver()).place(x=270, y=350)
        Button(width=11,height=4, text='(', relief='flat', bg='white', command=lambda: self.mostrar('(')).place(x=0,y=50)
        Button(width=11, height=4, text='C', relief='flat',bg="gray", command=self.limpar).place(x=0, y=350)

    def mostrar(self, valor):
        self.valor_entrada += str(valor)
        self.equacao.set(self.valor_entrada)

    def limpar(self):
        self.valor_entrada = ''
        self.equacao.set(self.valor_entrada)

    def resolver(self):
        resultado = eval(self.valor_entrada)
        self.equacao.set(resultado)


root = Tk()
Calculadora_simples = Calculadora(root)
root.mainloop()

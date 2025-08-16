import tkinter as tk
from tkinter import Frame, Label, Entry, Button

janela = tk.Tk()

def calcular_imc():
    imc= float(peso.get()) / float(altura.get()) **2
    resultado['text'] = f'O seu IMC é {imc:.2f}'
    print(f'O seu IMC é {imc:.2f}')



frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)
Label(frame, text='Para saber seu IMC, digite os valores abaixo:', pady=40).grid(column=1, row=1, columnspan=2)

Label(frame, text='Qual o seu peso?').grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)

Label(frame, text='Qual o sua altura?').grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular IMC', command=calcular_imc).grid(column=1, row=4, columnspan=2)
resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)




janela.title('Calculadora de IMC')
janela.mainloop()
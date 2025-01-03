from tkinter import *
from tkinter import ttk
import pyautogui as pg
import time
import csv
import pandas as pd
        
root = Tk()
root.title("Zabot")
root.minsize(800, 600)
label = ttk.Label(root, text="Bem vindo ao Zabot!", font=("Helvetica", 20), justify=CENTER)
label.pack()
label2 = ttk.Label(root, text="digite o nome do contato que queres mandar a mensagem abaixo", font=("Helvetica", 10), justify=CENTER)
label2.pack()
Imp = ttk.Entry(root)
Imp.pack()
label3 = ttk.Label(root, text="agora, digite a mensagem que deseja enviar", font=("Helvetica", 10), justify=CENTER)
label3.pack()
Imp2 = ttk.Entry(root)
Imp2.pack()
C = False
def data():
    global C
    C = True
    global cont 
    cont = Imp.get()
    global M
    M = Imp2.get()
    with open('CeM.csv', 'a') as f:
        w = csv.writer(f,dialect='excel-tab')
        w.writerow([cont, M])
botao = ttk.Button(root, text="salvar para enviar", command=data)
botao.pack()
botao = ttk.Button(root, text="Clique aqui para finalizar o envio", command=root.destroy)
botao.pack()
root.mainloop()
if C == True:
    pg.press('win')
    pg.write('whatsApp', interval=0.08)
    pg.press('enter')
    #pesquisa o contato
    time.sleep(2.8)
    pg.hotkey('ctrl' + 'F')
    pg.write(cont)
    #seleciona o contato
    pg.press('down')
    pg.press('enter')
    #manda a mensagem
    time.sleep(2)
    pg.click(x=1100, y=950)
    pg.write(M, interval=0.15)
    pg.press('enter')


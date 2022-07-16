from tkinter import *
from funçoes import *
#interface
root= Tk()

#criando frame
fr1 = Frame(root)
fr2 = Frame(root)
fr3= Frame(root)
#              cod= input('Insira o cod')
              #  nome= input('Insira o nome')
                #fabricante= input('Insira o fabricante')
               # quantia= input('Insira a quantia')
#criando label
opcoes = DBAgenda()
def salvar_produto(self, nome, fabricante, quantia):
    nome =ent()
    fabricante=ent1()
    quantia=ent2()
    opcoes.cadastrar_produtos(cod, nome, fabricante, quantia)

def listar():
    atributo = 'Estoque'
    list1= opcoes.listar_produtos(atributo)
    for i in list1:
        lbg_1['text'] += 'Cod: ' + str(i[0]) + ' ' + 'Prod: ' +str(i[1]) + '\n'
    return list1



lb0 = Label(fr1, text='ESTOQUE', font="Calibri 20", pady=30)
bt1 = Button (fr1, text='1 - Cadastrar produto', font="Calibri 14", command= lambda: [fr1.grid_remove(), fr2.grid(row=0, column=0)])
bt2 = Button (fr1, text='2 - Listar produto', font="Calibri 14")
bt3 = Button (fr1, text='3 - Procurar produto(COD)', font="Calibri 14", command= lambda: [fr1.grid_remove(), fr3.grid(row=0, column=0)])
cod= Entry (fr1)
bt4 = Button (fr1, text='4 - Alterar produto', font="Calibri 14")
bt5 = Button (fr1, text='5 - Sair', font="Calibri 14")



lbe=Label(fr2, text='Insira o nome:', font="Calibri 14")
lbe1=Label(fr2, text='Insira o fabricante:', font="Calibri 14")
lbe2=Label(fr2, text='Insira a quantia:', font="Calibri 14")
ent=Entry(fr2)
ent1=Entry(fr2)
ent2=Entry(fr2)
bte=Button(fr2, text='Cadastrar', font="Calibri 14", command=salvar_produto)


lbg_1 = Label(fr3, text='')
bty = Button(fr3, text='Listar Produtos', command= listar)

#layout
fr1.grid(row=0, column=0)
lb0.grid(row=0, column=0, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=2, column=0, sticky=NSEW)
bt3.grid(row=3, column=0, sticky=NSEW)
cod.grid(row=3, column=1, sticky=NSEW)
bt4.grid(row=4, column=0, sticky=NSEW)
bt5.grid(row=5, column=0, sticky=NSEW)

lbe.grid(row=0, column=0, sticky=NSEW)
lbe1.grid(row=1, column=0, sticky=NSEW)
lbe2.grid(row=2, column=0, sticky=NSEW)
ent.grid(row=0, column=1, sticky=NSEW)
ent1.grid(row=1,column=1, sticky=NSEW)
ent2.grid(row=2, column=1, sticky=NSEW)
bte.grid(row=3,column=0, sticky=NSEW)

lbg_1.grid(row=0,column=0,sticky=NSEW)
bty.grid(row=0,column=0,sticky=NSEW)
#mainloop
root.mainloop()

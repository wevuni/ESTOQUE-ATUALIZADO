from funçoes import *
from tkinter import *

class classe_menuu:
    def __init__(self):
        opcoes = DBAgenda()
        while True:
            entrada=input('1 - Cadastrar produto\n2 - Listar produtos\n3 - Procurar  produto\n4 - Alterar produto\n5- Sair')
            if entrada == '1':
                cod= input('Insira o cod')
                nome= input('Insira o nome')
                fabricante= input('Insira o fabricante')
                quantia= input('Insira a quantia')
                opcoes.cadastrar_produtos(cod, nome, fabricante, quantia)
            elif entrada == '2':
                opcoes.listar_produtos()
            elif entrada == '3':
                cod=input('Insira o código')
                opcoes.pesquisa_produto(cod)
            elif entrada == '4':
                linha=input('Insira a linha da mudança\n :')
                valor=input('Insira a mudança\n : ')
                cod=input('Insira o id a ser alterado\n : ')
                opcoes.alterar_tabela(linha, valor, cod)
            elif entrada == '0':
                break
            else:
                print ('Opção inválida!!!')
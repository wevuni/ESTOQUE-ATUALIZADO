import mysql.connector 
from info_produto import *
class DBAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='q1w2e3',
        database='vendas')
        self.meu_cursor = self.conexao.cursor()

    def cadastrar_produtos(self, cod, nome, fabricante, quantia):
        obj_produto = Info_produto(cod, nome, fabricante, quantia)
        comando_sql = f'insert into produtos ' \
                      f'(id, nome, fabricante, quantia) value ' \
                      f'("{obj_produto.cod}", "{obj_produto.nome}","{obj_produto.fabricante}","{obj_produto.quantia}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_produtos(self):
       comando_sql = f'select * from produtos'
       self.meu_cursor.execute(comando_sql)
       lista = self.meu_cursor.fetchall()
       for i in lista:
        print (i)
    
    def pesquisa_produto(self, cod):
        comando_sql=f'select * from produtos where id={cod}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print (i)
    
    def alterar_tabela(self, linha, valor, cod):
        comando_sql = f'update produtos set {linha} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
    
    

    
        
        
        

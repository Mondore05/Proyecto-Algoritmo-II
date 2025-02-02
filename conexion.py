import sqlite3

class conexion():
    def __init__(self):
    
        try:
          self.con = sqlite3.connect("pedidos.db")
          self.creartablas()
        except Exception as ex:
            print (ex)
    
    def creartablas(self):
        sql_create_table1 = """ CREATE TABLE IF NOT EXIST pedidos 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT UNIQUE, 
        nombre TEXT, clave TEXT)"""
        
        cur = self.con.cursor()
        cur.execute(sql_create_table1)

con = conexion()
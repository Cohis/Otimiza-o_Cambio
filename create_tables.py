import sqlite3

conn = sqlite3.connect("dados_banco.db")

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

#Tabela moedas

cursor.execute("""
                    CREATE TABLE IF NOT EXISTS moedas (
               
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL UNIQUE,
                    nome TEXT NOT NULL
               
               )

               """)

#Tabela instituições

cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS instituicoes (
               
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    pais TEXT NOT NULL
               
               )



""")

#Tabela clientes

cursor.execute("""

                    CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    pais TEXT NOT NULL,
                    perfil_risco TEXT NOT NULL
               )

""")



#Tabela operações

cursor.execute("""
CREATE TABLE IF NOT EXISTS operacoes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          cliente_id INTEGER,
          moeda_id INTEGER,
          instituicao_id INTEGER,
          tipo TEXT,
          valor REAL,
          data TEXT,

          FOREIGN KEY (cliente_id) REFERENCES clientes(id),
          FOREIGN KEY (insituicao_id) REFERENCES instituicoes(id),
          FOREIGN KEY (moeda_id) REFERENCES moedas(id)  
               
               )



""")


conn.commit()
conn.close()

print("Tabelas criadas com sucesso.")


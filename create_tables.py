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
          taxa REAL,
          data TEXT,
          

          FOREIGN KEY (cliente_id) REFERENCES clientes(id),
          FOREIGN KEY (instituicao_id) REFERENCES instituicoes(id),
          FOREIGN KEY (moeda_id) REFERENCES moedas(id)  
               
               )



""")

cursor.execute("""
          ALTER TABLE operacoes
          ADD COLUMN taxa REAL
""")

cursor.execute("""
     CREATE INDEX idx_operacoes_cliente_data
     ON operacoes(cliente_id, data DESC);

""")

cursor.execute("""

     CREATE INDEX idx_operacoes_data
     ON operacoes(data);

""")

cursor.execute("""
     CREATE INDEX idx_clientes_perfil
     ON clientes(perfil_risco);
""")

cursor.execute("""
     CREATE INDEX idx_operacoes_moeda
     ON operacoes (moeda_id);
""")


conn.commit()
conn.close()

print("Tabelas criadas com sucesso.")


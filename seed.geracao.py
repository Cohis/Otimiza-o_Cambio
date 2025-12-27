import sqlite3

#criar conexão com o banco de dados e preencher

conn = sqlite3.connect("dados_banco.db")
cursor = conn.cursor()

moedas = [
    ("USD", "Dólar Americano"),
    ("EUR", "Euro"),
    ("JPY", "Iene"),
    ("GBP", "Libra"),
    ("BRL", "Real")
]

cursor.executemany(
    "INSERT OR IGNORE INTO moedas (code, nome) VALUES (?,?)",
    moedas
)

instituicoes = [
    ("Banco Alpha", "Brasil"),
    ("Banco Beta", "EUA"),
    ("Exchange Gamma", "Reino Unido"),
    ("Banco Delta", "Alemanha")
]

cursor.executemany(
    "INSERT INTO instituicoes (nome, pais) VALUES (?, ?)",
    instituicoes
)

conn.commit()
conn.close()

print("Dados base inseridos.")
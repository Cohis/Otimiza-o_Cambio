import sqlite3

DB = "dados_banco.db"

def get_connection():
    conn = sqlite3.connect(DB)

    conn.row_factory = sqlite3.Row

    return conn


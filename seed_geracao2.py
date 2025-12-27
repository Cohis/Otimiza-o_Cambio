import sqlite3
import random

from datetime import datetime, timedelta
import time


DB_NAME = "dados_banco.db"
NUM_CLIENTES = 50_000
NUM_OPERACOES = 1_000_000
BATCH_SIZE = 10_000 #tamanho dos lotes de operações


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


# Otimizações de performance (APENAS PARA TESTES)
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("PRAGMA journal_mode = WAL")
cursor.execute("PRAGMA synchronous = NORMAL")

start_time = time.time()

#criar clientes:

perfis = ["BAIXO", "MEDIO", "ALTO"]
clientes = []


for i in range(NUM_CLIENTES):
    clientes.append(((f"Cliente{i}"), random.choice(["Brasil", "EUA", "Alemanha"]),
            random.choice(perfis)
            ))


cursor.executemany(
        "INSERT INTO clientes (nome, pais, perfil_risco) VALUES (?,?,?)",
        clientes
)

conn.commit()

print("Clientes criados com sucesso!")


cursor.execute("SELECT id FROM clientes")
clientes_id = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM moedas")
moedas_id = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM instituicoes")
instituicoes_id = [row[0] for row in cursor.fetchall()]


print("Criando operações")

base_date = datetime(2022, 1, 1)

for i in range(0, NUM_OPERACOES, BATCH_SIZE):
    operacoes = []

    for _ in range(BATCH_SIZE):
        data = base_date + timedelta(days=random.randint(0, 1000))
        operacoes.append((
            random.choice(clientes_id),
            random.choice(moedas_id),
            random.choice(instituicoes_id),
            random.choice(["COMPRA", "VENDA"]),
            round(random.uniform(1_000, 100_000), 2),
            round(random.uniform(4.5, 6.5), 4),
            data.strftime("%Y-%m-%d")
        ))

    cursor.executemany("""
        INSERT INTO operacoes
        (cliente_id, moeda_id, instituicao_id, tipo, valor, taxa, data)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, operacoes)

    conn.commit()
    print(f"{i + BATCH_SIZE} / {NUM_OPERACOES} operações inseridas")

# =========================
# FINALIZAÇÃO
# =========================

conn.close()

elapsed = time.time() - start_time
print(f"Carga pesada finalizada em {elapsed:.2f} segundos.")






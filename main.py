import sqlite3
import pandas as pd
from db import get_connection

conn = get_connection()

cursor = conn.cursor()

def historico_cliente():

    ide = input("Digite o id do cliente: ")

    query = """

            SELECT c.id , o.valor, m.code AS moeda, o.data

            FROM operacoes o
            JOIN clientes c ON c.id = o.cliente_id
            JOIN moedas m ON m.id = o.moeda_id

            WHERE c.id = ?

            ORDER BY o.data DESC

            LIMIT 10;
"""
    
    
    cursor.execute(query, (ide,))

    resultado = cursor.fetchall()

    if not resultado:
        print("Nenhum resultado encontrado")

    else:

        for ind, valor, codigo, data in resultado:
            print(f"{ind} | {valor} | {codigo} | {data}")



hoje = "2024-07-19"

def operacoes_hoje():

    query = """
        
        SELECT c.id, o.valor, m.code AS moeda, o.data

        FROM operacoes o
        JOIN clientes c ON c.id = o.cliente_id
        JOIN moedas m ON m.id = o.moeda_id

        WHERE DATE(o.data) = DATE(?)

"""
    cursor.execute(query, (hoje,))

    resultado = cursor.fetchall()

    if not resultado:
        print("Nenhum resultado encontrado")

    else:

        for ind, valor, codigo, data in resultado:
            print(f"{ind} | {valor} | {codigo} | {data}")


def ultimas():

    query = """
    
    SELECT c.id, o.valor, m.code AS moeda
    FROM operacoes o
    JOIN clientes c ON c.id = o.cliente_id
    JOIN moedas m ON m.id = o.moeda_id
    
    ORDER BY DATE(o.data) DESC
    LIMIT ?
    """

    limite = int(input("Digite o número de operações recentes que deseja ver: "))
    

    cursor.execute(query, (limite,))

    resultado = cursor.fetchall()

    for ind, valor, codigo in resultado:
        print(f"{ind} | {valor} | {codigo}")
    


def menu():

    

    print("\n========= BANCO DE DADOS CAMBIO =============")
    #na tabela 1, temos moedas (com id, código e nome) 
    #na tabela 2, instituições (com id, nome e país)
    #na tabela 3, temos clientes (id, nome, pais, perfil de risco)
    #na tabela 4, temos operacoes (id, cliente_id, moeda_id, instituicao_id, tipo, valor, taxa, data)
    
    print("1 - Histórico de operações")

    print("2- Operações de Hoje")

    print("3- Últimas N operações")
    
    print("4- Consultas de risco")

    print("5- Consultas gerenciais")




op = 0

while op != 9:
    
    menu()

    try:
        op = int(input("Escolha uma opção: "))
    
    except ValueError:
        print("Opção inválida")
        continue

    if op == 1:
        historico_cliente()

    elif op == 2:
        operacoes_hoje()

    elif op == 3:
        ultimas()

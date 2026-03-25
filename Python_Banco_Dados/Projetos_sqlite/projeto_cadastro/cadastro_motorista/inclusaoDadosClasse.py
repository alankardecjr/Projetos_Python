# -*- coding: utf-8 -*-
"""
Script para inserção dinâmica de dados nas tabelas Marca e Veiculo.
Utiliza queries parametrizadas e funções para otimizar e reutilizar código.
"""

import sqlite3 as conector
from modelo import Marca, Veiculo

def inserir_marca_dinamicamente(marca):
    """
    Insere uma marca no banco de dados e retorna o ID gerado.

    Args:
    - marca: Instância da classe Marca

    Returns:
    - ID da marca inserida
    """
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Query dinâmica para Marca (idempotente)
    comando = "INSERT OR IGNORE INTO Marca (nome, sigla) VALUES (:nome, :sigla);"
    cursor.execute(comando, {'nome': marca.nome, 'sigla': marca.sigla})

    if cursor.rowcount == 0:
        # marca já existe, recuperar id
        cursor.execute("SELECT id FROM Marca WHERE sigla = ?", (marca.sigla,))
        row = cursor.fetchone()
        marca_id = row[0] if row else None
        print(f"Marca {marca.nome} (sigla {marca.sigla}) já existe com ID {marca_id}.")
    else:
        marca_id = cursor.lastrowid
        print(f"Marca {marca.nome} inserida com sucesso com ID {marca_id}.")

    conexao.commit()
    cursor.close()
    conexao.close()

    return marca_id

def inserir_veiculo_dinamicamente(veiculo):
    """
    Insere um veículo no banco de dados.

    Args:
    - veiculo: Instância da classe Veiculo
    """
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")  # Habilita chaves estrangeiras
    cursor = conexao.cursor()

    # Query dinâmica para Veiculo (idempotente)
    comando = """
    INSERT OR IGNORE INTO Veiculo (placa, ano, cor, motor, proprietario, marca)
    VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);
    """
    valores = {
        'placa': veiculo.placa,
        'ano': veiculo.ano,
        'cor': veiculo.cor,
        'motor': veiculo.motor,
        'proprietario': veiculo.proprietario,
        'marca': veiculo.marca
    }
    cursor.execute(comando, valores)

    if cursor.rowcount == 0:
        print(f"Veículo {veiculo.placa} já existe e foi ignorado.")
    else:
        print(f"Veículo {veiculo.placa} inserido com sucesso!")

    conexao.commit()
    cursor.close()
    conexao.close()

# Exemplo de uso
if __name__ == "__main__":
    # Inserção de marcas
    marca1 = Marca(None, "Marca A", "MA")  # ID será gerado
    marca1.id = inserir_marca_dinamicamente(marca1)

    marca2 = Marca(None, "Marca B", "MB")
    marca2.id = inserir_marca_dinamicamente(marca2)

    # Inserção de veículos
    veiculos = [
        Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id),
        Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marca1.id),
        Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marca2.id),
        Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marca2.id)
    ]

    for veiculo in veiculos:
        inserir_veiculo_dinamicamente(veiculo)
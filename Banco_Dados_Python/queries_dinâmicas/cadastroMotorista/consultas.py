# -*- coding: utf-8 -*-
"""
Script para consultas dinâmicas no banco de dados.
Demonstra como realizar SELECTs parametrizados.
"""

import sqlite3 as conector

def consultar_pessoas():
    """
    Consulta todas as pessoas no banco.
    """
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = "SELECT cpf, nome, nascimento, oculos FROM Pessoa;"
    cursor.execute(comando)

    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(f"CPF: {pessoa[0]}, Nome: {pessoa[1]}, Nascimento: {pessoa[2]}, Óculos: {pessoa[3]}")

    cursor.close()
    conexao.close()

def consultar_veiculos_por_marca(marca_id):
    """
    Consulta veículos de uma marca específica de forma dinâmica.

    Args:
    - marca_id: ID da marca
    """
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = """
    SELECT v.placa, v.ano, v.cor, v.motor, p.nome
    FROM Veiculo v
    JOIN Pessoa p ON v.proprietario = p.cpf
    WHERE v.marca = ?;
    """
    cursor.execute(comando, (marca_id,))

    veiculos = cursor.fetchall()
    if veiculos:
        print(f"Veículos da marca {marca_id}:")
        for veiculo in veiculos:
            print(f"  Placa: {veiculo[0]}, Ano: {veiculo[1]}, Cor: {veiculo[2]}, Motor: {veiculo[3]}, Proprietário: {veiculo[4]}")
    else:
        print(f"Nenhum veículo encontrado para a marca {marca_id}.")

    cursor.close()
    conexao.close()

def consultar_marcas():
    """
    Consulta todas as marcas.
    """
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = "SELECT id, nome, sigla FROM Marca;"
    cursor.execute(comando)

    marcas = cursor.fetchall()
    for marca in marcas:
        print(f"ID: {marca[0]}, Nome: {marca[1]}, Sigla: {marca[2]}")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    print("=== Consultas no Banco de Dados ===\n")

    print("Pessoas cadastradas:")
    consultar_pessoas()
    print()

    print("Marcas cadastradas:")
    consultar_marcas()
    print()

    # Exemplo de consulta dinâmica por marca (usando ID 1 como exemplo)
    consultar_veiculos_por_marca(1)
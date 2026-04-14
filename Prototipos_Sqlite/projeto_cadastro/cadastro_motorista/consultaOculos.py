# -*- coding: utf-8 -*-
"""
Script para consultar pessoas que usam óculos.
"""

import sqlite3 as conector
from modelo import Pessoa

def consultar_pessoas_com_oculos():
    """
    Consulta todas as pessoas que usam óculos.
    """
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT cpf, nome, nascimento, oculos FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos registros
    registros = cursor.fetchall()
    if registros:
        print("Pessoas que usam óculos:")
        for registro in registros:
            pessoa = Pessoa(*registro)
            print(f"  CPF: {pessoa.cpf}, Nome: {pessoa.nome}, Nascimento: {pessoa.data_nascimento}, Óculos: {pessoa.usa_oculos}")
    else:
        print("Nenhuma pessoa com óculos cadastrada.")

    # Fechamento das conexões
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    consultar_pessoas_com_oculos()

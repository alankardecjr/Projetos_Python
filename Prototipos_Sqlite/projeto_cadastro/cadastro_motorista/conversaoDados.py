# -*- coding: utf-8 -*-
"""
Script para demonstrar conversão de dados do banco (BOOLEAN para Python bool).
Consulta pessoas que usam óculos com tratamento de tipos.
"""

import sqlite3 as conector
from modelo import Pessoa

def conv_bool(dado):
    """Converte valor do banco para booleano Python."""
    return True if dado == 1 else False

def consultar_pessoas_com_conversao():
    """
    Consulta pessoas que usam óculos com conversão de tipos.
    """
    # Registro de conversores
    conector.register_converter("BOOLEAN", conv_bool)
    
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT cpf, nome, nascimento, oculos FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos registros
    registros = cursor.fetchall()
    if registros:
        print("Pessoas que usam óculos (com conversão de tipos):\n")
        for registro in registros:
            pessoa = Pessoa(*registro)
            print(f"  CPF: {pessoa.cpf} (tipo: {type(pessoa.cpf).__name__})")
            print(f"  Nome: {pessoa.nome} (tipo: {type(pessoa.nome).__name__})")
            print(f"  Nascimento: {pessoa.data_nascimento} (tipo: {type(pessoa.data_nascimento).__name__})")
            print(f"  Óculos: {pessoa.usa_oculos} (tipo: {type(pessoa.usa_oculos).__name__})")
            print()
    else:
        print("Nenhuma pessoa com óculos encontrada.")

    # Fechamento das conexões
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    consultar_pessoas_com_conversao()
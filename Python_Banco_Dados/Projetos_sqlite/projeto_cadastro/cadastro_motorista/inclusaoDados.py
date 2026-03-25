# -*- coding: utf-8 -*-
"""
Script para inserção dinâmica de dados na tabela Pessoa.
Utiliza queries parametrizadas para evitar SQL injection e otimizar performance.
"""

import sqlite3 as conector
from modelo import Pessoa

def inserir_pessoa_dinamicamente(pessoa):
    """
    Insere uma pessoa no banco de dados de forma dinâmica.

    Args:
    - pessoa: Instância da classe Pessoa
    """
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Query dinâmica: construção da query com placeholders (idempotente)
    campos = ['cpf', 'nome', 'nascimento', 'oculos']
    placeholders = ':' + ', :'.join(campos)
    comando = f"INSERT OR IGNORE INTO Pessoa ({', '.join(campos)}) VALUES ({placeholders});"

    # Mapeamento dos valores
    valores = {
        'cpf': pessoa.cpf,
        'nome': pessoa.nome,
        'nascimento': pessoa.data_nascimento,
        'oculos': pessoa.usa_oculos
    }

    # Execução do comando
    cursor.execute(comando, valores)
    if cursor.rowcount == 0:
        print(f"Pessoa {pessoa.nome} (CPF {pessoa.cpf}) já existe e foi ignorada.")
    else:
        print(f"Pessoa {pessoa.nome} inserida com sucesso!")

    # Efetivação do comando
    conexao.commit()

    # Fechamento das conexões
    cursor.close()
    conexao.close()

    print(f"Pessoa {pessoa.nome} inserida com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    # Criação de um objeto do tipo Pessoa
    pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)

    # Inserção dinâmica
    inserir_pessoa_dinamicamente(pessoa)
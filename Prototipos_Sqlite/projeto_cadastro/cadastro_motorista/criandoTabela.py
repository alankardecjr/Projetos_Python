# -*- coding: utf-8 -*-
"""
Script para criação das tabelas no banco de dados SQLite.
Cria as tabelas Pessoa, Marca e Veiculo com suas respectivas chaves primárias e estrangeiras.
"""

import sqlite3 as conector

# Função para criar tabelas dinamicamente
def criar_tabelas():
    """
    Cria as tabelas no banco de dados.
    """
    # Abertura de conexão
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Comando SQL para criar tabela Pessoa
    comando_pessoa = '''
    CREATE TABLE IF NOT EXISTS Pessoa (
        cpf INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        nascimento TEXT NOT NULL,
        oculos BOOLEAN NOT NULL
    );
    '''

    # Comando SQL para criar tabela Marca
    comando_marca = '''
    CREATE TABLE IF NOT EXISTS Marca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL UNIQUE
    );
    '''

    # Comando SQL para criar tabela Veiculo
    comando_veiculo = '''
    CREATE TABLE IF NOT EXISTS Veiculo (
        placa TEXT PRIMARY KEY,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        motor REAL NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        FOREIGN KEY (proprietario) REFERENCES Pessoa (cpf),
        FOREIGN KEY (marca) REFERENCES Marca (id)
    );
    '''

    # Execução dos comandos
    cursor.execute(comando_pessoa)
    cursor.execute(comando_marca)
    cursor.execute(comando_veiculo)

    # Efetivação dos comandos
    conexao.commit()

    # Fechamento das conexões
    cursor.close()
    conexao.close()

    print("Tabelas criadas com sucesso!")

# Chamada da função
if __name__ == "__main__":
    criar_tabelas()

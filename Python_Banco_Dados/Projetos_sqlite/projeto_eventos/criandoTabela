"""
Módulo para gerenciamento de eventos com SQLite.

Este script cria um banco de dados SQLite para armazenar informações sobre locais, eventos e participantes.
"""

import sqlite3

def conectar_banco(Agenda_Eventos):
    """
    Conecta ao banco de dados SQLite especificado.

    Args:
        nome_banco (str): Nome do arquivo do banco de dados.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados.
    """
    conexao = sqlite3.connect(Agenda_Eventos)
    return conexao

def criar_tabelas(conexao):
    """
    Cria as tabelas necessárias no banco de dados se elas não existirem.

    As tabelas criadas são:
    - Locais: Armazena informações sobre os locais dos eventos.
    - Eventos: Armazena informações sobre os eventos.
    - Participantes: Armazena informações sobre os participantes dos eventos.

    Args:
        conexao (sqlite3.Connection): Conexão com o banco de dados.
    """
    cursor = conexao.cursor()
   
    # Cria a tabela Locais
    cursor.execute('''CREATE TABLE IF NOT EXISTS Locais (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      endereco TEXT NOT NULL)''')
   
    # Cria a tabela Eventos
    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      data TEXT NOT NULL,
                      local_id INTEGER NOT NULL,
                      FOREIGN KEY(local_id) REFERENCES Locais(id))''')
   
    # Cria a tabela Participantes
    cursor.execute('''CREATE TABLE IF NOT EXISTS Participantes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL,
                      evento_id INTEGER NOT NULL,
                      FOREIGN KEY(evento_id) REFERENCES Eventos(id))''')
   
    conexao.commit()

if __name__ == '__main__':
    # Conecta ao banco de dados
    conexao = conectar_banco('eventos.db')
    # Cria as tabelas
    criar_tabelas(conexao)
    # Fecha a conexão
    conexao.close()



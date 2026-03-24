import sqlite3
import json
import sys

# Script de inclusão de dados fictícios para o banco de dados `eventos.db`.
# As tabelas devem existir (criado em `criandoTabela`).
# Inclui validação de foreign keys, consultas e entrada configurável.


def conectar_banco(banco='eventos.db'):
    """Conecta ao banco SQLite com validação de foreign keys ativada."""
    conexao = sqlite3.connect(banco)
    # Ativa validação de foreign keys para garantir integridade referencial.
    # Isso impede inserções com FKs inválidas (ex: evento_id inexistente).
    conexao.execute('PRAGMA foreign_keys = ON')
    return conexao


def inserir_dados_ficticios(conexao, dados=None):
    """
    Insere dados de exemplo em Locais, Eventos e Participantes.

    Args:
        conexao: Conexão SQLite ativa.
        dados: Dicionário opcional com dados customizados. Se None, usa dados padrão.
    """
    if dados is None:
        # Dados fictícios padrão (hardcoded como fallback).
        dados = {
            'locais': [
                ('Auditório Central', 'Rua A, 123 - Itinga'),
                ('Teatro Municipal', 'Av. B, 456 - Vilas do Atlântico'),
                ('Espaço de Convenções', 'Av beira rio, nº 10 - Centro')
            ],
            'eventos': [
                ('Festival de Python', '2026-04-10', 1),
                ('Hackathon Educação', '2026-05-20', 2),
                ('Feira de Tecnologia', '2026-06-15', 3)
            ],
            'participantes': [
                ('Ana Silva', 'ana.silva@email.com', 1),
                ('Bruno Costa', 'bruno.costa@email.com', 1),
                ('Carla Souza', 'carla.souza@email.com', 2),
                ('Diego Lima', 'diego.lima@email.com', 3)
            ]
        }

    cursor = conexao.cursor()

    # Inserção de registros na tabela Locais.
    # Usa INSERT OR IGNORE para evitar duplicação em reexecuções.
    cursor.executemany(
        'INSERT OR IGNORE INTO Locais (nome, endereco) VALUES (?, ?)',
        dados['locais']
    )

    # Inserção de registros na tabela Eventos (depende de Locais).
    cursor.executemany(
        'INSERT OR IGNORE INTO Eventos (nome, data, local_id) VALUES (?, ?, ?)',
        dados['eventos']
    )

    # Inserção de registros na tabela Participantes (depende de Eventos).
    cursor.executemany(
        'INSERT OR IGNORE INTO Participantes (nome, email, evento_id) VALUES (?, ?, ?)',
        dados['participantes']
    )

    # Commit garante persistência no arquivo físico do banco.
    conexao.commit()


def consultar_eventos_com_participantes(conexao):
    """
    Consulta e exibe eventos com seus participantes e locais.

    Retorna uma lista de dicionários com dados agregados.
    """
    cursor = conexao.cursor()

    # Query JOIN para obter dados relacionados.
    # LEFT JOIN inclui eventos sem participantes.
    query = '''
    SELECT
        e.id AS evento_id,
        e.nome AS evento_nome,
        e.data AS evento_data,
        l.nome AS local_nome,
        l.endereco AS local_endereco,
        p.nome AS participante_nome,
        p.email AS participante_email
    FROM Eventos e
    JOIN Locais l ON e.local_id = l.id
    LEFT JOIN Participantes p ON e.id = p.evento_id
    ORDER BY e.data, e.id, p.nome
    '''

    cursor.execute(query)
    resultados = cursor.fetchall()

    # Agrupa resultados por evento (já que LEFT JOIN pode duplicar linhas).
    eventos_agrupados = {}
    for row in resultados:
        evento_id = row[0]
        if evento_id not in eventos_agrupados:
            eventos_agrupados[evento_id] = {
                'id': row[0],
                'nome': row[1],
                'data': row[2],
                'local': {'nome': row[3], 'endereco': row[4]},
                'participantes': []
            }

        # Adiciona participante se existir (não None).
        if row[5] is not None:
            eventos_agrupados[evento_id]['participantes'].append({
                'nome': row[5],
                'email': row[6]
            })

    return list(eventos_agrupados.values())


def carregar_dados_de_json(caminho_json):
    """
    Carrega dados customizados de um arquivo JSON.

    Args:
        caminho_json: Caminho para arquivo JSON com estrutura de dados.

    Returns:
        Dicionário com dados ou None se erro.
    """
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar JSON: {e}")
        return None


def main():
    """Função principal com argumentos de linha de comando."""
    # Argumentos: python inclusaoDados.py [--json caminho.json] [--consultar]
    args = sys.argv[1:]

    # Conecta ao banco (sempre necessário).
    conexao = conectar_banco('eventos.db')

    try:
        if '--consultar' in args:
            # Modo consulta: exibe eventos e participantes.
            eventos = consultar_eventos_com_participantes(conexao)
            print("=== EVENTOS CADASTRADOS ===")
            for evento in eventos:
                print(f"\nEvento: {evento['nome']} ({evento['data']})")
                print(f"Local: {evento['local']['nome']} - {evento['local']['endereco']}")
                print(f"Participantes ({len(evento['participantes'])}):")
                for p in evento['participantes']:
                    print(f"  - {p['nome']} ({p['email']})")
                if not evento['participantes']:
                    print("  (Nenhum participante cadastrado)")

        else:
            # Modo inserção: dados padrão ou de JSON.
            dados_customizados = None
            if '--json' in args:
                idx = args.index('--json')
                if idx + 1 < len(args):
                    caminho_json = args[idx + 1]
                    dados_customizados = carregar_dados_de_json(caminho_json)

            # Insere dados (padrão ou customizados).
            inserir_dados_ficticios(conexao, dados_customizados)
            print("Dados fictícios inseridos com sucesso!")

    finally:
        # Sempre fecha a conexão.
        conexao.close()


if __name__ == '__main__':
    # Executar `criandoTabela.py` antes deste script para criar o schema.
    main()


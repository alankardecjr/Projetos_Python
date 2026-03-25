# -*- coding: utf-8 -*-
"""
Script principal para o sistema de cadastro de motoristas.
Executa a criação de tabelas e inserção de dados de forma otimizada.
"""

import os
import argparse
from criandoTabela import criar_tabelas
from inclusaoDados import inserir_pessoa_dinamicamente
from inclusaoDadosClasse import inserir_marca_dinamicamente, inserir_veiculo_dinamicamente
from modelo import Pessoa, Marca, Veiculo

DB_PATH = "./meu_banco.db"

def main(reset=False):
    """
    Função principal que orquestra a criação do banco e inserção de dados.
    """
    if reset:
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
            print(f"Banco de dados removido: {DB_PATH}")
        else:
            print(f"Banco de dados não existe ainda: {DB_PATH}")

    print("Iniciando criação do banco de dados...")

    # 1. Criar tabelas
    criar_tabelas()
    # 2. Inserir pessoas (dados fictícios)
    pessoas = [
        Pessoa(10000000099, 'João Silva', '1985-01-15', False),
        Pessoa(20000000099, 'José Santos', '1990-02-28', False),
        Pessoa(30000000099, 'Maria Oliveira', '1990-03-30', True),
        Pessoa(40000000099, 'Ana Pereira', '1988-05-12', False),
        Pessoa(50000000099, 'Carlos Souza', '1992-07-20', True),
        Pessoa(60000000099, 'Fernanda Lima', '1987-09-10', False),
        Pessoa(70000000099, 'Roberto Costa', '1995-11-05', True),
        Pessoa(80000000099, 'Patrícia Alves', '1991-12-18', False),
        Pessoa(90000000099, 'Lucas Ferreira', '1989-04-22', True),
        Pessoa(10000000100, 'Juliana Rodrigues', '1993-06-14', False)
    ]

    for pessoa in pessoas:
        inserir_pessoa_dinamicamente(pessoa)

    # 3. Inserir marcas e veículos
    marcas = [
        ("Fiat", "FIAT"),
        ("Volkswagen", "VW"),
        ("Chevrolet", "CHEV"),
        ("Ford", "FORD"),
        ("Toyota", "TOYO"),
        ("Honda", "HOND"),
        ("Renault", "RENA"),
        ("Nissan", "NISS")
    ]

    marcas_ids = []
    for nome, sigla in marcas:
        marca = Marca(None, nome, sigla)
        marca.id = inserir_marca_dinamicamente(marca)
        marcas_ids.append(marca.id)

    # Inserção de veículos fictícios
    veiculos = [
        Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marcas_ids[0]),  # Fiat
        Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marcas_ids[1]),  # VW
        Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marcas_ids[2]), # Chevrolet
        Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marcas_ids[3]),   # Ford
        Veiculo("EAA0005", 2010, "Vermelho", 1.6, 40000000099, marcas_ids[4]), # Toyota
        Veiculo("FAA0006", 2011, "Cinza", 1.8, 50000000099, marcas_ids[5]),   # Honda
        Veiculo("GAA0007", 2012, "Verde", 2.0, 60000000099, marcas_ids[6]),   # Renault
        Veiculo("HAA0008", 2013, "Amarelo", 1.5, 70000000099, marcas_ids[7]), # Nissan
        Veiculo("IAA0009", 2014, "Roxo", 1.4, 80000000099, marcas_ids[0]),    # Fiat
        Veiculo("JAA0010", 2015, "Laranja", 2.5, 90000000099, marcas_ids[1]), # VW
        Veiculo("KAA0011", 2016, "Marrom", 1.0, 10000000100, marcas_ids[2]), # Chevrolet
        Veiculo("LAA0012", 2017, "Rosa", 1.8, 10000000099, marcas_ids[3]),    # Ford
        Veiculo("MAA0013", 2018, "Bege", 2.0, 20000000099, marcas_ids[4]),   # Toyota
        Veiculo("NAA0014", 2019, "Turquesa", 1.6, 30000000099, marcas_ids[5]), # Honda
        Veiculo("OAA0015", 2020, "Dourado", 1.4, 40000000099, marcas_ids[6])  # Renault
    ]

    for veiculo in veiculos:
        inserir_veiculo_dinamicamente(veiculo)

    print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cadastro de motoristas com opção de reset do banco")
    parser.add_argument("--reset", action="store_true", help="Apaga o banco de dados e recria as tabelas")
    args = parser.parse_args()

    main(reset=args.reset)

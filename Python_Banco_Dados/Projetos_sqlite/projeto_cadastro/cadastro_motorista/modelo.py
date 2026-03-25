# -*- coding: utf-8 -*-
"""
Módulo de definição de classes para o sistema de cadastro de motoristas.
Contém as classes Pessoa, Marca e Veiculo.
"""

class Pessoa:
    """
    Classe que representa uma pessoa no sistema.
    Atributos:
    - cpf: CPF da pessoa (inteiro)
    - nome: Nome da pessoa (string)
    - data_nascimento: Data de nascimento (string no formato YYYY-MM-DD)
    - usa_oculos: Indica se usa óculos (booleano)
    - veiculos: Lista de veículos associados (inicialmente vazia)
    """
    def __init__(self, cpf, nome, data_nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.usa_oculos = usa_oculos
        self.veiculos = []  # Lista para armazenar veículos associados

class Marca:
    """
    Classe que representa uma marca de veículo.
    Atributos:
    - id: ID da marca (inteiro)
    - nome: Nome da marca (string)
    - sigla: Sigla da marca (string)
    """
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

class Veiculo:
    """
    Classe que representa um veículo.
    Atributos:
    - placa: Placa do veículo (string)
    - ano: Ano de fabricação (inteiro)
    - cor: Cor do veículo (string)
    - motor: Potência do motor (float)
    - proprietario: CPF do proprietário (inteiro)
    - marca: ID da marca (inteiro)
    """
    def __init__(self, placa, ano, cor, motor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca
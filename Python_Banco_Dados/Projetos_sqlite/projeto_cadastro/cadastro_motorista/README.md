# Sistema de Cadastro de Motoristas

Este projeto é um sistema simples de cadastro de motoristas usando Python e SQLite. Ele demonstra o uso de classes, queries dinâmicas e operações CRUD básicas.

## Estrutura do Projeto

- `modelo.py`: Definições das classes Pessoa, Marca e Veiculo.
- `criandoTabela.py`: Script para criação das tabelas no banco de dados.
- `inclusaoDados.py`: Script para inserção dinâmica de pessoas.
- `inclusaoDadosClasse.py`: Script para inserção dinâmica de marcas e veículos.
- `main.py`: Script principal que executa todo o processo.
- `consultas.py`: Script para consultas dinâmicas no banco de dados.

## Como Usar

1. Execute `python main.py` para criar o banco e inserir dados fictícios.
2. Execute `python consultas.py` para visualizar os dados inseridos e exemplos de consultas dinâmicas.
3. Os dados são armazenados em `meu_banco.db`.

## Funcionalidades

- **Queries Dinâmicas**: Uso de placeholders para evitar SQL injection em inserts e selects.
- **Comentários**: Código bem documentado com docstrings.
- **Otimização**: Funções reutilizáveis e estrutura modular.
- **Dados Fictícios**: Inclui 10 pessoas, 8 marcas e 15 veículos de exemplo.
- **Consultas**: Exemplos de SELECTs parametrizados para leitura de dados.

## Dados Incluídos

- **Pessoas**: 10 motoristas fictícios com CPFs, nomes, datas de nascimento e informação sobre uso de óculos.
- **Marcas**: 8 marcas de veículos populares (Fiat, VW, Chevrolet, etc.).
- **Veículos**: 15 veículos com placas, anos, cores, motores e associações a proprietários e marcas.

## Dependências

- Python 3.x
- SQLite (incluído no Python)
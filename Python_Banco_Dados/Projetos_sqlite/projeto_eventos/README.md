# Gerenciamento de Eventos - Scripts Python com SQLite

Este projeto contém scripts para gerenciar um banco de dados de eventos usando SQLite.

## Arquivos

- `criandoTabela`: Cria as tabelas do banco de dados `eventos.db`
- `inclusaoDados`: Insere dados fictícios e permite consultas
- `dados_customizados.json`: Exemplo de dados customizados em JSON

## Funcionalidades Implementadas

### 1. Validação de Foreign Keys
- Ativa `PRAGMA foreign_keys = ON` para garantir integridade referencial
- Impede inserções com chaves estrangeiras inválidas

### 2. Função de Consulta
- `consultar_eventos_com_participantes()`: Lista eventos com participantes e locais
- Usa JOIN para combinar dados das 3 tabelas
- Exibe resultados agrupados por evento

### 3. Dados Configuráveis
- Dados padrão (hardcoded) como fallback
- Suporte a dados customizados via arquivo JSON
- Argumentos de linha de comando para diferentes modos

## Como Usar

### 1. Criar as Tabelas
```bash
python criandoTabela
```

### 2. Inserir Dados Padrão
```bash
python inclusaoDados
```

### 3. Inserir Dados Customizados
```bash
python inclusaoDados --json dados_customizados.json
```

### 4. Consultar Dados
```bash
python inclusaoDados --consultar
```

## Estrutura do Banco

### Tabelas
- **Locais**: id, nome, endereco
- **Eventos**: id, nome, data, local_id (FK)
- **Participantes**: id, nome, email, evento_id (FK)

### Relacionamentos
- Eventos → Locais (1:N)
- Participantes → Eventos (1:N)

## Exemplo de Saída da Consulta

```
=== EVENTOS CADASTRADOS ===

Evento: Festival de Python (2026-04-10)
Local: Auditório Central - Rua A, 123 - Centro
Participantes (2):
  - Ana Silva (ana.silva@email.com)
  - Bruno Costa (bruno.costa@email.com)

Evento: Hackathon Educação (2026-05-20)
Local: Teatro Municipal - Av. B, 456 - Vila Nova
Participantes (1):
  - Carla Souza (carla.souza@email.com)
```

## Formato JSON Customizado

```json
{
  "locais": [
    ["Nome do Local", "Endereço completo"]
  ],
  "eventos": [
    ["Nome do Evento", "YYYY-MM-DD", local_id]
  ],
  "participantes": [
    ["Nome", "email@exemplo.com", evento_id]
  ]
}
```

## Boas Práticas Implementadas

- Uso de `INSERT OR IGNORE` para evitar duplicatas
- Tratamento adequado de conexões (abrir/fechar)
- Validação de foreign keys
- Estrutura modular com funções reutilizáveis
- Tratamento de erros para arquivos JSON
- Documentação completa com docstrings
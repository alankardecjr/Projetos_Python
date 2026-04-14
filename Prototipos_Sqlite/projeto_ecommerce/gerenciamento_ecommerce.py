import sqlite3
from datetime import datetime

class GerenciamentoEcommerce:
    """
    Classe para gerenciar um banco de dados SQLite de ecommerce.
    Inclui operações para produtos, clientes e pedidos.
    """

    def __init__(self, nome_banco='ecommerce.db'):
        """
        Inicializa a conexão com o banco de dados.
        """
        self.nome_banco = nome_banco
        self.conexao = None

    def conectar(self):
        """
        Estabelece conexão com o banco de dados.
        """
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            print(f"Conectado ao banco de dados '{self.nome_banco}'.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")
            raise

    def desconectar(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def criar_tabelas(self):
        """
        Cria as tabelas necessárias: Produtos, Clientes, Pedidos.
        """
        if not self.conexao:
            raise ValueError("Conexão não estabelecida. Chame conectar() primeiro.")

        cursor = self.conexao.cursor()

        # Tabela Produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                preco REAL NOT NULL CHECK(preco > 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0)
            )
        ''')

        # Tabela Clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        # Tabela Pedidos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL CHECK(quantidade > 0),
                data_pedido TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                FOREIGN KEY (produto_id) REFERENCES Produtos(id)
            )
        ''')

        self.conexao.commit()
        print("Tabelas criadas com sucesso.")

    def inserir_produto(self, nome, preco, estoque):
        """
        Insere um novo produto na tabela Produtos.
        """
        if not self.conexao:
            raise ValueError("Conexão não estabelecida.")

        cursor = self.conexao.cursor()
        try:
            cursor.execute('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)',
                           (nome, preco, estoque))
            self.conexao.commit()
            print(f"Produto '{nome}' inserido com sucesso.")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir produto: {e}")

    def inserir_cliente(self, nome, email):
        """
        Insere um novo cliente na tabela Clientes.
        """
        if not self.conexao:
            raise ValueError("Conexão não estabelecida.")

        cursor = self.conexao.cursor()
        try:
            cursor.execute('INSERT INTO Clientes (nome, email) VALUES (?, ?)',
                           (nome, email))
            self.conexao.commit()
            print(f"Cliente '{nome}' inserido com sucesso.")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir cliente: {e}")

    def inserir_pedido(self, cliente_id, produto_id, quantidade):
        """
        Insere um novo pedido na tabela Pedidos.
        Verifica se há estoque suficiente.
        """
        if not self.conexao:
            raise ValueError("Conexão não estabelecida.")

        cursor = self.conexao.cursor()

        # Verificar estoque
        cursor.execute('SELECT estoque FROM Produtos WHERE id = ?', (produto_id,))
        resultado = cursor.fetchone()
        if not resultado or resultado[0] < quantidade:
            print("Estoque insuficiente para o pedido.")
            return

        # Inserir pedido
        data_pedido = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            cursor.execute('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)',
                           (cliente_id, produto_id, quantidade, data_pedido))
            # Atualizar estoque
            cursor.execute('UPDATE Produtos SET estoque = estoque - ? WHERE id = ?',
                           (quantidade, produto_id))
            self.conexao.commit()
            print("Pedido inserido e estoque atualizado.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir pedido: {e}")

    def inserir_dados_iniciais(self):
        """
        Insere dados iniciais de exemplo.
        """
        # Produtos
        produtos = [
            ('Notebook', 2999.99, 10),
            ('Smartphone', 1999.99, 20),
            ('Tablet', 999.99, 30)
        ]
        for nome, preco, estoque in produtos:
            self.inserir_produto(nome, preco, estoque)

        # Clientes
        clientes = [
            ('Alice', 'alice@example.com'),
            ('Bob', 'bob@example.com'),
            ('Charlie', 'charlie@example.com')
        ]
        for nome, email in clientes:
            self.inserir_cliente(nome, email)

        # Pedidos (usando IDs existentes)
        self.inserir_pedido(1, 1, 2)
        self.inserir_pedido(2, 2, 1)
        self.inserir_pedido(3, 3, 3)

if __name__ == '__main__':
    # Exemplo de uso
    gerenciador = GerenciamentoEcommerce()
    gerenciador.conectar()
    gerenciador.criar_tabelas()
    gerenciador.inserir_dados_iniciais()
    gerenciador.desconectar()        



import database
import random
from datetime import datetime

def popular_banco():
    print("=== Iniciando Povoamento do Banco de Dados ===")
    
    # 1. Criar as tabelas primeiro
    database.criar_tabelas()

    # --- 20 CLIENTES ---
    clientes_fake = [
        ("Maria Silva", "11988887771", "1990-05-15", 35, "Rua das Flores", 10, "Centro", "São Paulo", "Perto do Mercado", "Cliente VIP"),
        ("Ana Oliveira", "11988887772", "1985-08-20", 36, "Av. Brasil", 500, "Jardins", "São Paulo", "Prédio Azul", ""),
        ("Carla Souza", "11988887773", "1992-12-10", 37, "Rua Chile", 12, "Mooca", "São Paulo", "", "Gosta de brilho"),
        ("Juliana Lima", "11988887774", "1988-03-05", 34, "Rua B", 102, "Lapa", "São Paulo", "Frente à praça", ""),
        ("Patricia Meira", "11988887775", "1995-07-25", 38, "Travessa Paz", 5, "Itaim", "São Paulo", "", ""),
        ("Fernanda Costa", "11988887776", "1980-01-30", 35, "Rua 7 de Setembro", 45, "Centro", "Osasco", "", "Idosa"),
        ("Beatriz Santos", "11988887777", "1998-11-12", 36, "Av. Paulista", 1500, "Bela Vista", "São Paulo", "Conjunto Nacional", ""),
        ("Sandra Rocha", "11988887778", "1975-06-18", 39, "Rua Augusta", 80, "Cerqueira César", "São Paulo", "", ""),
        ("Renata Alves", "11988887779", "1991-09-09", 37, "Rua da Consolação", 200, "Centro", "São Paulo", "", ""),
        ("Monica Pereira", "11988887780", "1987-04-22", 35, "Rua Vergueiro", 1010, "Vila Mariana", "São Paulo", "", "PCD"),
        ("Lúcia Ferreira", "11988887781", "1960-02-14", 38, "Rua Domingos", 22, "Saúde", "São Paulo", "", ""),
        ("Amanda Nunes", "11988887782", "1993-10-01", 34, "Rua Joaquim", 33, "Cambuci", "São Paulo", "", ""),
        ("Vanessa Guedes", "11988887783", "1989-11-20", 36, "Rua Independência", 44, "Ipiranga", "São Paulo", "Perto do Museu", ""),
        ("Tatiana Mello", "11988887784", "1984-05-05", 37, "Av. Jabaquara", 55, "Jabaquara", "São Paulo", "", ""),
        ("Bruna Vieira", "11988887785", "1996-08-08", 35, "Rua Santa Cruz", 66, "Vila Mariana", "São Paulo", "", ""),
        ("Camila Diniz", "11988887786", "1991-12-25", 36, "Rua Turiassu", 77, "Perdizes", "São Paulo", "", ""),
        ("Debora Silva", "11988887787", "1982-03-15", 38, "Av. Sumaré", 88, "Pompeia", "São Paulo", "", ""),
        ("Erika Ramos", "11988887788", "1990-06-06", 35, "Rua Clélia", 99, "Lapa", "São Paulo", "", ""),
        ("Priscila Kato", "11988887789", "1988-07-07", 34, "Rua Heitor Penteado", 111, "Sumaré", "São Paulo", "", ""),
        ("Leticia Spiller", "11988887790", "1985-02-02", 37, "Av. Angélica", 222, "Higienópolis", "São Paulo", "", "Inativo")
    ]

    for c in clientes_fake:
        try:
            database.salvar_cliente(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9])
        except: pass # Evitar erro se o script rodar duas vezes por causa do UNIQUE

    # --- 20 PRODUTOS ---
    produtos_fake = [
        ("Sapatilha Verniz Preta", "Preta", "35", 40.0, 89.90, 10, "Casual", "Fabrica A"),
        ("Sapatilha Matelassê Bege", "Bege", "36", 45.0, 95.00, 15, "Clássico", "Fabrica B"),
        ("Mule Bico Fino Caramelo", "Caramelo", "37", 50.0, 110.00, 8, "Mule", "Fabrica A"),
        ("Sapatilha Boneca Vermelha", "Vermelha", "34", 42.0, 85.00, 5, "Casual", "Fabrica C"),
        ("Scarpin Nude Salto Baixo", "Nude", "38", 60.0, 150.00, 12, "Festa", "Fabrica B"),
        ("Sapatilha Glitter Prata", "Prata", "36", 48.0, 99.00, 7, "Festa", "Fabrica C"),
        ("Sapatilha Camurça Azul", "Azul", "37", 38.0, 79.90, 20, "Promoção", "Fabrica A"),
        ("Rasteira Pedraria", "Dourada", "35", 35.0, 75.00, 10, "Verão", "Fabrica D"),
        ("Sapatilha Floral", "Estampada", "36", 40.0, 89.90, 6, "Primavera", "Fabrica D"),
        ("Sapatilha Bico Fino Branca", "Branca", "37", 45.0, 95.00, 4, "Noiva", "Fabrica B"),
        ("Mule Animal Print", "Onça", "38", 55.0, 120.00, 9, "Mule", "Fabrica A"),
        ("Sapatilha Laço Clássico", "Rosa", "35", 40.0, 89.90, 11, "Casual", "Fabrica C"),
        ("Sapatilha Confort Soft", "Cinza", "39", 50.0, 105.00, 14, "Confort", "Fabrica E"),
        ("Sapatilha Jeans", "Azul", "36", 35.0, 70.00, 18, "Casual", "Fabrica E"),
        ("Scarpin Preto Camurça", "Preto", "37", 65.0, 160.00, 5, "Festa", "Fabrica B"),
        ("Sapatilha Verniz Nude", "Nude", "35", 40.0, 89.90, 10, "Casual", "Fabrica A"),
        ("Rasteira Nó Marrom", "Marrom", "38", 30.0, 65.00, 12, "Verão", "Fabrica D"),
        ("Sapatilha Metalizada Ouro", "Ouro", "36", 48.0, 99.90, 7, "Festa", "Fabrica C"),
        ("Sapatilha Alpargata", "Verde", "37", 30.0, 60.00, 15, "Casual", "Fabrica E"),
        ("Mule Soft White", "Branco", "34", 50.0, 115.00, 6, "Mule", "Fabrica A")
    ]

    for p in produtos_fake:
        try:
            database.salvar_item(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        except: pass

    # --- 10 VENDAS ---
    formas_pag = ["Pix", "Cartão Crédito", "Dinheiro", "Cartão Débito"]
    
    # Buscar IDs existentes para garantir a integridade
    clientes_ids = [c[0] for c in database.listar_clientes()]
    produtos_ids = [p[0] for p in database.listar_itens()]

    if clientes_ids and produtos_ids:
        for _ in range(10):
            c_id = random.choice(clientes_ids)
            p_id = random.choice(produtos_ids)
            
            # Cada venda terá de 1 a 2 produtos aleatórios
            # Pegando o preço de venda do banco para o produto selecionado
            conn = database.conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT precovenda FROM itens WHERE id = ?", (p_id,))
            preco = cursor.fetchone()[0]
            conn.close()

            lista_venda = [(p_id, 1, preco)] # ID, Qtd, Preço Unitário
            database.registrar_venda(c_id, lista_venda, random.choice(formas_pag), "Pago", "Entregue")

    print("=== Banco de Dados Populado com Sucesso! ===")

if __name__ == "__main__":
    popular_banco()
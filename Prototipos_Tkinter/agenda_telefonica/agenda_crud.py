import os
import psycopg2
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()

DB_URL = os.getenv("DATABASE_URL", "dbname=postgres user=admin password=1234 host=localhost port=5432")

def executar_sql(sql, params=None, fetch=False):
    try:
        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                if fetch:
                    return cur.fetchall()
            conn.commit()
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None


def inserir():
    nome, tel = input("Nome: "), input("Telefone: ")
    executar_sql("INSERT INTO agenda (nome, telefone) VALUES (%s, %s)", (nome, tel))
    print("✅ Contato salvo!")

def listar():
    contatos = executar_sql("SELECT * FROM agenda ORDER BY id", fetch=True)
    print("\n--- CONTATOS ---")
    for c in (contatos or []):
        print(f"[{c[0]}] {c[1]} - {c[2]}")

def atualizar():
    idx = input("ID do contato: ")
    nome, tel = input("Novo Nome (vazio para manter): "), input("Novo Tel (vazio para manter): ")
    
    atual = executar_sql("SELECT nome, telefone FROM agenda WHERE id = %s", (idx,), fetch=True)
    if atual:
        executar_sql("UPDATE agenda SET nome=%s, telefone=%s WHERE id=%s", 
                     (nome or atual[0][0], tel or atual[0][1], idx))
        print("✅ Atualizado!")

def deletar():
    idx = input("ID para remover: ")
    executar_sql("DELETE FROM agenda WHERE id = %s", (idx,))
    print("🗑️ Removido!")

def main():
    executar_sql("CREATE TABLE IF NOT EXISTS agenda (id SERIAL PRIMARY KEY, nome TEXT, telefone TEXT)")

    menu = {
        "1": ("Inserir", inserir),
        "2": ("Listar", listar),
        "3": ("Atualizar", atualizar),
        "4": ("Deletar", deletar),
        "5": ("Sair", exit)
    }

    while True:
        print("\n--- AGENDA POSTGRES ---")
        for k, v in menu.items():
            print(f"{k}. {v[0]}")
        
        opcao = input("Selecione: ")
        if opcao in menu:
            menu[opcao][1]()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
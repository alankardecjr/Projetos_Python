import os
import psycopg2
from faker import Faker
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

if os.path.exists(".env"):
    try:
        load_dotenv(encoding='utf-8')
    except UnicodeDecodeError:
        load_dotenv(encoding='latin-1')

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    user = os.getenv("DB_USER", "admin")
    pw = os.getenv("DB_PASSWORD", "1234")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME", "postgres")
    DB_URL = f"dbname={db} user={user} password={pw} host={host} port={port}"

fake = Faker('pt_BR')

def popular_banco(total=40):
    schema_sql = """
    CREATE TABLE IF NOT EXISTS agenda (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        telefone VARCHAR(30) NOT NULL
    );
    """
    insert_sql = "INSERT INTO agenda (nome, telefone) VALUES (%s, %s)"

    try:
        with psycopg2.connect(DB_URL) as conn:
            conn.set_client_encoding('UTF8')
            
            with conn.cursor() as cursor:
                cursor.execute(schema_sql)
                
                dados = []
                for _ in range(total):
                    dados.append((fake.name(), fake.phone_number()))
                
                cursor.executemany(insert_sql, dados)
                
            conn.commit()
            print(f"✅ Sucesso! {total} contatos inseridos sem erros de codec.")

    except Exception as e:
        print(f"❌ Erro ao processar o banco: {e}")

if __name__ == "__main__":
    popular_banco(40)
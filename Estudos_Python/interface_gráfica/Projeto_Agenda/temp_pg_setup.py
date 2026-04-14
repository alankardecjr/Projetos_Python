from pathlib import Path

roles_sql = """CREATE ROLE admin LOGIN PASSWORD '1234';
ALTER ROLE admin WITH LOGIN PASSWORD '1234';
ALTER ROLE postgres WITH PASSWORD 'Kardec24';
DROP DATABASE IF EXISTS alan;
"""
Path('pg_roles.sql').write_text(roles_sql, encoding='utf-8')

create_db_sql = 'CREATE DATABASE "Alan Kardec" OWNER admin;\n'
Path('pg_create_db.sql').write_text(create_db_sql, encoding='utf-8')
print('SQL files generated')

# continuaçao do arquivo sql indice
import sqlite3

# Função para criar os índices no banco de dados
def create_indexes():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('stafftracker.db')
    cursor = conn.cursor()

    # Abrir o arquivo de índices e executar os comandos SQL
    with open('create_indexes.sql', 'r') as file:
        cursor.executescript(file.read())  # Executa o script SQL

    conn.commit()

    conn.close()

    print("Índices criados com sucesso!")

# Executando a função
if __name__ == "__main__":
    create_indexes()

python create_indexes.py
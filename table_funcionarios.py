''' 
database
sqlite3 database.db 
'''
import sqlite3
from datetime import datetime, timedelta

def conectar():
    return sqlite3.connect('database.db')

def calcular_proximo_sabado():
  hoje = datetime.now()
  dias_para_proximo_sabado = (5 - hoje.weekday()) % 7
  proximo_sabado = hoje + timedelta(days=dias_para_proximo_sabado)
  return proximo_sabado.strftime('%d/%m/%Y') # Retorna a data formatada como string

# Função para criar a tabela 'plantao' se não existir
def criar_tabela():
  conexao = conectar() #conectando ao banco
  cursor = conexao.cursor() #criar cursor para comandos SQL
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS plantao (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      data TEXT NOT NULL
    )
  """)
  conexao.commit() 
  conexao.close() 

  print("Cadastro concluído com sucesso!")

def adicionar_funcionario(nome):
    conexao = conectar()
    cursor = conexao.cursor() # Criando um cursor para executar comandos SQL

    # Inserindo os dados na tabela 'plantao'
    cursor.execute("INSERT INTO plantao (nome) VALUES (?)", (nome,))
    
    conexao.commit()  # Confirmando as alterações no banco
    conexao.close()  # Fechando a conexão

    print(f"Funcionário {nome} adicionado com sucesso!")

# Criando a tabela, se não existir
criar_tabela()

# teste add funcionario
nome = input("Digite o nome do funcionário: ").strip()
if nome:
    adicionar_funcionario(nome)
else:
    print("Nome inválido. Por favor, insira um nome válido.")

   






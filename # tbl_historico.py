# tbl_historico
import sqllite3
conn = sqlite3.connect('stafftracker.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS HISTORICO (
   id interger primary key autoincrement,
   funcionario_id integer not null,
   plantao_id integer not null, 
   acao text not null, -- exemplo: 'adicionado', 'removido', 'alterado'
   data_modificacao text not null default current_timestamp,
   foreign key (funcionario_id) references funcionarios(id),
   foreign key (plantao_id) references plantao(id)
);
''')
conn.commit()
conn.close()
# tbl escala 
import sqllite3
conn = sqllite.connect('stafftracker.db')
cursor = conn.cursor()
cursor.execute('''
create table if not exists escala (
  id integer primary key autoincrement,
  funcionario_id integer not null,
  plantao_id integer not null,
  status text not null default 'Confirmado', -- ex: 'Confirmado', 'Não confirmado'
  foreign key (funcionario_id) references funcionarios(id),
  foreign key (plantao_id) references plantao(id)
);
''')
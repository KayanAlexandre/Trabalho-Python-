import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE ALUNOS (
               id integer primary key autoincrement,
               nome text,
               nota real
) 
               """)
cursor.execute("""
insert into alunos(nome,nota)
values(?,?)
""",( "Naytan", 8.5)               )
cursor.execute("""
insert into alunos(nome,nota)
values(?,?)
""",( "Caio", 5.5)               )
cursor.execute("""
insert into alunos(nome,nota)
values(?,?)
""",( "Richard", 7.5)               )
conexao.commit()
conexao.close()
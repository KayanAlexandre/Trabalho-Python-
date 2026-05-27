import sqlite3
import json
try:
    conexao = sqlite3.connect(
        "vendas.db"
    )
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT,
        valor REAL,
        data_venda TEXT
    )
    """)
    conexao.commit()
    cursor.execute("""
    INSERT INTO vendas(
        produto,
        valor,
        data_venda
    )
    VALUES
    ('Mouse', 120.50, '2026-01-10'),
    ('Teclado', 250.00, '2026-01-15'),
    ('Monitor', 900.00, '2026-02-20'),
    ('Notebook', 3500.00, '2026-02-25')
    """)
    conexao.commit()
    cursor.execute("""
    SELECT
        substr(data_venda, 1, 7) AS mes,
        COUNT(*) AS total_vendas,
        SUM(valor) AS valor_total

    FROM vendas
    GROUP BY mes
    ORDER BY mes
    """)
    resultados = cursor.fetchall()
    relatorio = {
        "ano": 2026,
        "meses": []
    }
    for linha in resultados:
        mes = linha[0]
        total_vendas = linha[1]
        valor_total = linha[2]
        relatorio["meses"].append({
            "mes": mes,
            "total_vendas": total_vendas,
            "valor_total": valor_total
        })
    with open("relatorio_ano_2026.json","w",encoding="utf-8") as arquivo_json:
        json.dump(relatorio,arquivo_json,indent=4, ensure_ascii=False )
    print( "Relatório gerado com sucesso!")
except sqlite3.Error as erro:
    print( f"Erro no banco: {erro}")
except json.JSONDecodeError:
    print( "Erro ao gerar JSON")
finally:
    conexao.close()
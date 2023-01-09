import sqlite3 as sq

with sq.connect("aircrafts.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS aircrafts (
        avion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        year INTEGER,
        author TEXT
    )
    """)

    cur.execute("INSERT INTO aircrafts VALUES(1, 'Биплан Докучаева', 1910, 'А.Я. Докучаев')")
    cur.execute("INSERT INTO aircrafts VALUES(2, 'Гаккель-VIII', 1912, 'Я.М. Гаккель')")
    cur.execute("INSERT INTO aircrafts VALUES(3, 'С-6Б', 1912, 'И.И. Сикорский')")
    cur.execute("INSERT INTO aircrafts VALUES(4, 'Русский Витязь', 1913, 'И.И. Сикорский')")
    cur.execute("INSERT INTO aircrafts VALUES(5, 'Лебедь-12', 1915, 'В.А. Лебедев')")

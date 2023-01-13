import sqlite3 as sq

aircraft = [
    ('Би-Кок', 1914, 'А.А. Пороховщиков'),
    ('Четырёхплан Савельева', 1916, 'В.Ф. Савельев'),
    ('ИМ-Б поплавковый', 1914, 'И.И. Сикорский'),
    ('Святогор', 1916, 'В.А. Слесарев'),
    ('Летающая лодка М-5', 1915, 'Д.П. Григорович')
]

avions = [
    ('Конек-Горбунок', 1923, 'В.Н. Хиони'),
    ('ДФ-1', 1922, 'Д.Д. Фёдоров'),
    ('АК-1', 1923, 'Александров и Калинин')
]

with sq.connect("aircraft.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS aircraft (
        avion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        year INTEGER,
        author TEXT
    )
    """)
    cur.execute("DELETE FROM aircraft WHERE avion_id LIKE '14'")

    cur.executescript("""
    DELETE FROM aircraft WHERE avion_id LIKE '15';
    DELETE FROM aircraft WHERE avion_id LIKE '16';
    INSERT INTO aircraft VALUES(NULL, 'У-2', 1928, 'Н.Н. Поликарпов');
    INSERT INTO aircraft VALUES(NULL, 'БИЧ-7', 1929, 'Б.И.Черановский')
    """)

    cur.execute("UPDATE aircraft SET year = :Year WHERE model LIKE 'Св%'", {'Year': 1915})

    cur.executemany("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", models)

    for avion in models:
        cur.execute("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", avion)

    for aircr in aircraft:
        cur.execute("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", aircr)


    cur.execute("INSERT INTO aircraft VALUES(1, 'Биплан Докучаева', 1910, 'А.Я. Докучаев')")
    cur.execute("INSERT INTO aircraft VALUES(2, 'Гаккель-VIII', 1912, 'Я.М. Гаккель')")
    cur.execute("INSERT INTO aircraft VALUES(3, 'С-6Б', 1912, 'И.И. Сикорский')")
    cur.execute("INSERT INTO aircraft VALUES(4, 'Русский Витязь', 1913, 'И.И. Сикорский')")
    cur.execute("INSERT INTO aircraft VALUES(5, 'Лебедь-12', 1915, 'В.А. Лебедев')")

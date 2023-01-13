import sqlite3 as sq

aircraft = [
    ('��-���', 1914, '�.�. ������������'),
    ('���������� ���������', 1916, '�.�. ��������'),
    ('��-� �����������', 1914, '�.�. ���������'),
    ('��������', 1916, '�.�. ��������'),
    ('�������� ����� �-5', 1915, '�.�. ����������')
]

avions = [
    ('�����-��������', 1923, '�.�. �����'),
    ('��-1', 1922, '�.�. Ը�����'),
    ('��-1', 1923, '����������� � �������')
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
    INSERT INTO aircraft VALUES(NULL, '�-2', 1928, '�.�. ����������');
    INSERT INTO aircraft VALUES(NULL, '���-7', 1929, '�.�.�����������')
    """)

    cur.execute("UPDATE aircraft SET year = :Year WHERE model LIKE '��%'", {'Year': 1915})

    cur.executemany("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", models)

    for avion in models:
        cur.execute("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", avion)

    for aircr in aircraft:
        cur.execute("INSERT INTO aircraft VALUES(NULL, ?, ?, ?)", aircr)


    cur.execute("INSERT INTO aircraft VALUES(1, '������ ���������', 1910, '�.�. ��������')")
    cur.execute("INSERT INTO aircraft VALUES(2, '�������-VIII', 1912, '�.�. �������')")
    cur.execute("INSERT INTO aircraft VALUES(3, '�-6�', 1912, '�.�. ���������')")
    cur.execute("INSERT INTO aircraft VALUES(4, '������� ������', 1913, '�.�. ���������')")
    cur.execute("INSERT INTO aircraft VALUES(5, '������-12', 1915, '�.�. �������')")

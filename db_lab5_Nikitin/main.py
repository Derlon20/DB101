import psycopg2 
import matplotlib.pyplot as plt

username = 'postgres'
password = 'localhost'
database = 'test 2'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

create_timegame_view = """
    CREATE OR REPLACE VIEW time_game AS
SELECT g.name, g.time
FROM Game g
ORDER BY Time DESC;
"""
cur.execute(create_timegame_view)


create_domainpie_view = """
    CREATE OR REPLACE VIEW domainpie AS
    SELECT D.domain, COUNT(DG.Game_id) AS GameCount
FROM Domains D
LEFT JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
GROUP BY D.domain
ORDER BY GameCount DESC;
"""
cur.execute(create_domainpie_view)


create_domaintime_view = """
    CREATE OR REPLACE VIEW domaintime AS
SELECT D.domain, AVG(G.Time) AS AverageTime
FROM Domains D
JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
JOIN Game G ON DG.Game_id = G.Game_id
GROUP BY D.domain
ORDER BY AverageTime DESC;
"""
cur.execute(create_domaintime_view)


cur.close()

query_a = "select * from time_game;"
query_b = "select * from domainpie;"
query_c = "select * from domaintime;"

with conn:
    cur = conn.cursor()

    cur.execute(query_a)
    a = cur.fetchall()

    cur.execute(query_b)
    b = cur.fetchall()

    cur.execute(query_c)
    c = cur.fetchall()

    labels_a = [row[0] for row in a]
    values_a = [row[1] for row in a]
    labels_2b = [row[1] for row in b]
    values_2b = [row[0] for row in b]
    time = [row[1] for row in c]
    domain = [row[0] for row in c]


    plt.figure(figsize=(10, 6))
    bars = plt.barh(labels_a, values_a, color='lightgreen')
    plt.xlabel('Time Spent (minutes)')
    plt.title('Time Spent on Games')
    for bar, game in zip(bars, labels_a):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, game, ha='left', va='center')

    plt.grid(axis='x') 

    plt.savefig('a.png')

    plt.figure(figsize = (10, 8))
    plt.pie(labels_2b, labels = values_2b, autopct = '%1.1f%%', startangle = 140)
    plt.legend()
    plt.title('Розподіл ігор за жанрами')
    plt.savefig('b.png')


    plt.figure(figsize=(10, 6))
    bar=plt.bar(domain, time, color='skyblue')
    for bar, avg_time in zip(bars, time):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5, f'{avg_time:.2f}', 
             ha='center', va='top', fontsize=8, color='darkblue')
    plt.title('Середній час гри кожного жанру')

    plt.savefig('c.png')
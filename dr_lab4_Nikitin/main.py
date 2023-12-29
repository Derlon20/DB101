import psycopg2 

username = 'postgres'
password = 'localhost'
database = 'LR3'
host = 'localhost'
port = '5432'


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cur = conn.cursor()


query_a = """
SELECT g.name, g.time
FROM Game g
ORDER BY Time DESC;
"""

cur.execute(query_a)
result_a = cur.fetchall()

print("Query_a result:")

for row in result_a:
    print(row)

query_b = """
    SELECT D.domain, COUNT(DG.Game_id) AS GameCount
FROM Domains D
LEFT JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
GROUP BY D.domain
ORDER BY GameCount DESC;
"""

cur.execute(query_b)
result_b = cur.fetchall()

print("Query_b result:")

for row in result_b:
    print(row)

query_c = '''
SELECT D.domain, AVG(G.Time) AS AverageTime
FROM Domains D
JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
JOIN Game G ON DG.Game_id = G.Game_id
GROUP BY D.domain
ORDER BY AverageTime DESC;
'''
cur.execute(query_c)
result_c = cur.fetchall()

print("Query_c result:")

for row in result_c:
    print(row)

cur.close()
conn.close()
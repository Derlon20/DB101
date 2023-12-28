import psycopg2 
import matplotlib.pyplot as plt

username = 'postgres'
password = 'localhost'
database = 'lr4'
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

print("Query_с result:")

for row in result_c:
    print(row)

cur.close()
conn.close()





labels_a = [row[0] for row in result_a]
values_a = [row[1] for row in result_a]

plt.figure(figsize=(10, 6))
bars = plt.barh(labels_a, values_a, color='lightgreen')
plt.xlabel('Time Spent (minutes)')
plt.title('Time Spent on Games')
for bar, game in zip(bars, labels_a):
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, game, ha='left', va='center')

plt.grid(axis='x') 
plt.show()




labels_2b = [row[1] for row in result_b]
values_2b = [row[0] for row in result_b]

plt.figure(figsize = (9, 8))
plt.pie(labels_2b, labels = values_2b, autopct = '%1.1f%%', startangle = 140)
plt.title('Розподіл ігор за жанрами')
plt.show()




time = [row[1] for row in result_c]
domain = [row[0] for row in result_c]

plt.figure(figsize=(10, 6))
bar=plt.bar(domain, time, color='skyblue')
for bar, avg_time in zip(bars, time):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5, f'{avg_time:.2f}', 
             ha='center', va='top', fontsize=8, color='darkblue')
plt.title('Середній час гри кожного жанру')
plt.xlabel('Жанр')
plt.ylabel('Average Time (minutes)')
plt.show()
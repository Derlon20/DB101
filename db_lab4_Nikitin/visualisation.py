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
select name, time from game
order by time desc;
"""

cur.execute(query_a)
result_a = cur.fetchall()

print("Query_a result:")

for row in result_a:
    print(row)





query_b = """
select domain, count(domain_of_game.Game_id) as GameCount
from Domains
left join domain_of_game on domains.domain_id = domain_of_game.domain_id
group by domains.domain
order by GameCount desc;
"""

cur.execute(query_b)
result_b = cur.fetchall()

print("Query_b result:")

for row in result_b:
    print(row)



query_c = '''
select domain, avg(game.time) as AverageTime from domains 
join domain_of_game on domains.domain_id = domain_of_game.domain_id
join game on domain_of_game.game_id = game.game_id
group by domains.domain
order by AverageTime desc;
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
plt.show()

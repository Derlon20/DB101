import psycopg2
import json

username = 'postgres'
password = 'localhost'
database = 'test 2'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

table_names = ['game', 'domain_of_game', 'domains']


data = {}
with conn:

    cur = conn.cursor()
    
    for table in table_names:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('export_json.json', 'w') as outf:
    json.dump(data, outf, default = str)
    
import sqlite3
conn = sqlite3.connect('blog.db')
cur = conn.cursor()

query = '''select * from blogpost;'''
cur.execute(query)
rows = cur.fetchall()

for i in rows:
    print(type(i))

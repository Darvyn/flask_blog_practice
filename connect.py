import sqlite3
conn = sqlite3.connect('blog.db')
cur = conn.cursor()

query_del = '''delete from blogpost where id=4;'''
cur.execute(query_del)

query = '''select * from blogpost;'''
cur.execute(query)
rows = cur.fetchall()

for row in rows:
  print(row)



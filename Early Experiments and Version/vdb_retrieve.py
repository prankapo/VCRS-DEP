import sqlite3

conn = sqlite3.connect('Voyager1.sqlite3')
cur = conn.cursor()

cur.execute("SELECT Time, Flux_1, Flux_2, Flux_3, Flux_4 FROM Flux WHERE Time >= '1998-06-01 06:00:00' LIMIT 10")
row = cur.fetchmany(5)
count = 1
for item in row :
    print(count, '.' , item)
    count = count + 1
cur.close()